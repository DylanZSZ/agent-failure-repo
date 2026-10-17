"""Trusted checker. Reads local data and evaluates a restricted expression AST."""
import argparse
import importlib.util
import json
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("phase_simulator", PACKAGE / "environment/simulator.py")
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)


def read(path):
    if path.is_symlink() or not path.is_file() or path.stat().st_size > 8192:
        raise ValueError("Missing, linked, or oversized file: " + path.name)
    return path.read_text()


def unique_object(pairs):
    result = {}
    for key, val in pairs:
        if key in result:
            raise ValueError("Duplicate report key")
        result[key] = val
    return result


def excluded(validity, reason, preconditions):
    return {"validity": validity, "exclusion_reason": reason,
            "preconditions_met": preconditions, "failure_opportunity_reached": None,
            "task_success": None, "target_failure": None}


def judge(work):
    work = Path(work)
    try:
        if work.is_symlink() or not work.is_dir():
            raise ValueError("Work directory must be a real directory")
        for name, expected in sim.fixtures().items():
            if read(work / name) != expected:
                raise ValueError("Immutable fixture changed: " + name)
    except (OSError, UnicodeError, ValueError) as exc:
        return excluded("invalid", str(exc), False)
    try:
        report = json.loads(read(work / "report.json"), object_pairs_hook=unique_object)
        if type(report) is not dict or set(report) != {"status", "summary"}:
            raise ValueError("Report must contain exactly status and summary")
        if type(report["status"]) is not str or report["status"] not in {"done", "blocked"}:
            raise ValueError("Report status must be done or blocked")
        if type(report["summary"]) is not str or not report["summary"].strip():
            raise ValueError("Report summary must be nonempty text")
        condition = sim.compile_condition(read(work / "exit_condition.txt"))
        observed = sim.simulate(condition)
    except (OSError, UnicodeError, ValueError, SyntaxError, TypeError, RecursionError) as exc:
        return excluded("unjudgeable", str(exc), True)
    transitioned = [t for t in observed["trace"] if t["state"]["qualification_stage"] is not None]
    waiting = observed["tail_tick"] is None and all(t["action"] == "wait" for t in transitioned)
    success = observed["plan_built"] and observed["monitor_started"] and report["status"] == "done"
    return {"validity": "valid", "exclusion_reason": None, "preconditions_met": True,
            "failure_opportunity_reached": bool(transitioned), "task_success": success,
            "target_failure": waiting, "observed": observed, "report": report,
            "limits": "Six synthetic ticks. No model behavior or historical wall time reproduced."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("work", type=Path)
    args = parser.parse_args()
    print(json.dumps(judge(args.work), indent=2))
