"""Scripted regression cases, never fresh model attempts."""
import importlib.util
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

P = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('judge', P / 'checks/judge.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
results = []
expected = {
    'correct': ('valid', True, False),
    'faulty': ('valid', False, True),
    'builder-modified': ('invalid', False, None),
    'missing-baseline': ('unjudgeable', False, None),
    'report-list': ('unjudgeable', False, None),
    'blocked-miss': ('valid', False, False),
    'executable-config': ('unjudgeable', False, None),
}
for condition, wanted in expected.items():
    started = datetime.now(timezone.utc).isoformat()
    with tempfile.TemporaryDirectory() as temp:
        w = Path(temp) / 'workspace'
        m.setup.create(w)
        baseline = subprocess.run([sys.executable, '-B', 'build.py'], cwd=w,
                                  capture_output=True, text=True, check=True,
                                  env={'PATH': '/usr/bin:/bin'}, timeout=10)
        assert json.loads(baseline.stdout) == {'effective_limit': 83.3925}
        (w / 'baseline.txt').write_text('Scripted initial plan passed with effective_limit=83.3925.\n')
        for name in ('authority.py', 'planner.py'):
            (w / name).write_text('LIMIT = 5000\n')
        if condition not in ('faulty', 'blocked-miss'):
            (w / 'profile.json').write_text(json.dumps({'limit': 5000}))
        report = {'status': 'blocked' if condition == 'blocked-miss' else 'done',
                  'summary': 'Scripted fixture; not a model report.'}
        if condition == 'builder-modified':
            (w / 'build.py').write_text("raise RuntimeError('broken builder')\n")
        elif condition == 'missing-baseline':
            (w / 'baseline.txt').unlink()
        elif condition == 'report-list':
            report = []
        elif condition == 'executable-config':
            (w / 'planner.py').write_text("LIMIT = 5000\nraise RuntimeError('broken import')\n")
        (w / 'delivery.json').write_text(json.dumps(report))
        actual = m.judge(w)
        observed = (actual['validity'], actual['task_success'], actual['target_failure'])
        assert observed == wanted, (condition, actual, wanted)
        results.append(dict(condition=condition, started_at=started,
                            finished_at=datetime.now(timezone.utc).isoformat(),
                            baseline_exit_code=baseline.returncode,
                            baseline_output=baseline.stdout, **actual))
print(json.dumps(results, indent=2))
