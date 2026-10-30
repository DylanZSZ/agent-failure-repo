#!/usr/bin/env python3
"""Read only lines admitted by a private, fingerprinted fixed-page freeze."""

import argparse
import hashlib
import json
from pathlib import Path

from history import Projection, human_queued_command_lines, redact_long_strings, summarize_visible_page


def load_freeze(path):
    freeze = json.loads(Path(path).read_text(encoding="utf-8"))
    source = Path(freeze["source_path_private"])
    expected_sha = freeze["sha256"].lower()
    line_count = int(freeze["physical_lines"])
    page_size = int(freeze["page_size"])
    starts = freeze["page_starts"]
    bounded_limit = freeze.get("bounded_page_char_limit")
    provider = freeze.get("provider") or freeze.get("source_id", "").split("-", 1)[0]
    if not source.is_absolute() or line_count < 1 or page_size < 1:
        raise ValueError("freeze needs an absolute source and positive line/page counts")
    if provider not in ("claude", "codex") or len(expected_sha) != 64 or any(c not in "0123456789abcdef" for c in expected_sha):
        raise ValueError("freeze needs a provider and SHA-256")
    if not isinstance(starts, list) or not starts or any(type(x) is not int for x in starts):
        raise ValueError("freeze page_starts must be nonempty integer list")
    if starts != sorted(set(starts)) or any(x < 1 or x > line_count or (x - 1) % page_size for x in starts):
        raise ValueError("freeze page_starts must be unique, sorted, aligned and in range")
    if bounded_limit is not None and (type(bounded_limit) is not int or bounded_limit < 1):
        raise ValueError("bounded_page_char_limit must be a positive integer")
    return source, expected_sha, line_count, page_size, starts, provider, bounded_limit


def verified_lines(source, expected_sha, line_count, first=None, last=None):
    """Buffer an allowed range, then verify the entire source before emitting it."""
    sha = hashlib.sha256()
    actual_lines = 0
    selected = []
    with source.open("rb") as stream:
        for actual_lines, raw in enumerate(stream, 1):
            sha.update(raw)
            if first is not None and first <= actual_lines <= last:
                selected.append((actual_lines, raw))
    if actual_lines != line_count or sha.hexdigest() != expected_sha:
        raise ValueError("source line count or SHA-256 differs from freeze")
    return selected


def read_allowed(source, expected_sha, count, page_size, starts, provider,
                 bounded_limit=None, page=None, line=None):
    if page is not None:
        if page not in starts:
            raise ValueError("requested page is outside frozen page_starts")
        first, last = page, min(count, page + page_size - 1)
    elif line is not None:
        if line < 1 or line > count or not any(start <= line < start + page_size for start in starts):
            raise ValueError("requested line is outside frozen pages")
        first = last = line
    else:
        raise ValueError("choose a frozen page or an allowed line")
    projection = Projection()
    events, errors = [], []
    for number, raw in verified_lines(source, expected_sha, count, first, last):
        projection.line = number
        try:
            record = json.loads(raw)
        except (ValueError, UnicodeError, RecursionError):
            errors.append({"line": number, "error": "invalid_json"})
            projection.omit("invalid_json")
            continue
        if not isinstance(record, dict):
            errors.append({"line": number, "error": "non_object_record"})
            projection.omit("non_object_record")
            continue
        event = projection.claude(record) if provider == "claude" else projection.codex(record)
        if event is not None:
            events.append(event)
    return {"start_line": first, "end_line": last, "physical_lines": last - first + 1,
            "provider": provider, "events": events,
            "human_queued_command_lines": human_queued_command_lines(events),
            "omissions": dict(projection.omissions),
            "omission_anchors": projection.omission_anchors,
            "schema_gaps": projection.gaps, "errors": errors,
            "reading_note": "Only allowlisted visible events are projected; omissions are not reviewed evidence."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--freeze", type=Path, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true", help="Verify freeze and report ranges, without reading source text")
    action.add_argument("--page", type=int, help="Read exactly one frozen page by its listed start line")
    action.add_argument("--summary", type=int, metavar="PAGE",
                        help="Inventory one frozen page, including long projected fields, without event bodies")
    action.add_argument("--line", type=int, help="Read one line inside any frozen page")
    args = parser.parse_args()
    try:
        source, expected_sha, count, page_size, starts, provider, bounded_limit = load_freeze(args.freeze)
        if args.check:
            verified_lines(source, expected_sha, count)
            print(json.dumps({"physical_lines": count, "page_size": page_size,
                              "page_ranges": [[x, min(count, x + page_size - 1)] for x in starts]},
                             sort_keys=True))
        else:
            result = read_allowed(source, expected_sha, count, page_size, starts, provider,
                                  bounded_limit=bounded_limit,
                                  page=args.page if args.summary is None else args.summary,
                                  line=args.line)
            if args.summary is not None:
                result = summarize_visible_page(result)
            elif args.page is not None and bounded_limit is not None:
                result = redact_long_strings(result, bounded_limit)
            print(json.dumps(result, indent=2, ensure_ascii=False))
    except (KeyError, TypeError, ValueError, OSError, json.JSONDecodeError) as exc:
        parser.exit(1, f"Frozen-page read rejected: {exc}\n")


if __name__ == "__main__":
    main()
