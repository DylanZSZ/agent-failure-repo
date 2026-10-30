"""Check that fixed-page reads cannot emit source lines outside a freeze."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


COMMAND = Path(__file__).resolve().parents[1] / "commands/frozen_pages.py"


class FrozenPageTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.source = self.base / "source.jsonl"
        self.records = [
            {"type": "response_item", "payload": {"type": "message", "role": "user",
                "content": [{"type": "input_text", "text": "VISIBLE_USER"}]}},
            {"type": "response_item", "payload": {"type": "reasoning",
                "summary": [{"type": "summary_text", "text": "HIDDEN_REASONING"}]}},
            {"type": "response_item", "payload": {"type": "message", "role": "assistant",
                "channel": "final", "content": [{"type": "output_text", "text": "OUTSIDE_PAGE"}]}},
            {"type": "response_item", "payload": {"type": "message", "role": "assistant",
                "channel": "analysis", "content": [{"type": "output_text", "text": "OUTSIDE_ANALYSIS"}]}},
            {"type": "unrecognized_record", "payload": {"text": "HIDDEN_UNKNOWN"}},
            {"type": "response_item", "payload": {"type": "message", "role": "assistant",
                "channel": "final", "content": [{"type": "output_text", "text": "VISIBLE_FINAL"}]}},
            {"type": "response_item", "payload": {"type": "message", "role": "assistant",
                "channel": "final", "content": [{"type": "output_text", "text": "OUTSIDE_END"}]}},
        ]
        self.write_source()
        self.freeze = self.base / "freeze.json"
        self.write_freeze()

    def write_source(self):
        self.source.write_text("\n".join(json.dumps(x) for x in self.records) + "\n", encoding="utf-8")

    def write_freeze(self, **changes):
        value = {
            "source_path_private": str(self.source),
            "provider": "codex",
            "sha256": hashlib.sha256(self.source.read_bytes()).hexdigest(),
            "physical_lines": 7,
            "page_size": 2,
            "page_starts": [1, 5],
        }
        value.update(changes)
        self.freeze.write_text(json.dumps(value), encoding="utf-8")

    def call(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(COMMAND), "--freeze", str(self.freeze), *args],
            cwd=self.base, capture_output=True, text=True, check=False,
        )

    def test_check_and_allowed_reads(self):
        check = self.call("--check")
        self.assertEqual(check.returncode, 0, check.stderr)
        self.assertEqual(json.loads(check.stdout)["page_ranges"], [[1, 2], [5, 6]])
        first = json.loads(self.call("--page", "1").stdout)
        self.assertEqual(first["start_line"], 1)
        self.assertEqual(first["end_line"], 2)
        self.assertIn("VISIBLE_USER", json.dumps(first))
        self.assertNotIn("HIDDEN_REASONING", json.dumps(first))
        self.assertEqual(first["omission_anchors"][0]["line"], 2)
        second = json.loads(self.call("--page", "5").stdout)
        self.assertIn("VISIBLE_FINAL", json.dumps(second))
        self.assertNotIn("HIDDEN_UNKNOWN", json.dumps(second))
        self.assertNotIn("OUTSIDE_PAGE", json.dumps(second))
        self.assertNotIn("OUTSIDE_END", json.dumps(second))
        self.assertEqual(second["omission_anchors"][0]["line"], 5)
        self.assertEqual(json.loads(self.call("--line", "6").stdout)["events"][0]["line"], 6)

    def test_rejects_displaced_page_and_nearby_lines(self):
        for args in (("--page", "3"), ("--line", "3"), ("--line", "4"), ("--line", "7"), ("--line", "0")):
            with self.subTest(args=args):
                result = self.call(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")

    def test_rejects_changed_source_and_invalid_freeze(self):
        self.records[0]["payload"]["content"][0]["text"] = "CHANGED_USER"
        self.write_source()
        result = self.call("--line", "1")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.records[0]["payload"]["content"][0]["text"] = "VISIBLE_USER"
        self.write_source()
        self.write_freeze(page_starts=[1, 4])
        self.assertNotEqual(self.call("--check").returncode, 0)

    def test_claude_uses_the_same_visible_projection(self):
        self.records = [
            {"type": "user", "sessionId": "s", "message": {"role": "user", "content": "CLAUDE_USER"}},
            {"type": "assistant", "sessionId": "s", "message": {"role": "assistant",
                "content": [{"type": "thinking", "thinking": "CLAUDE_PRIVATE"}]}},
            {"type": "user", "sessionId": "s", "message": {"role": "user", "content": "OUTSIDE_PAGE"}},
            {"type": "user", "sessionId": "s", "message": {"role": "user", "content": "OUTSIDE_PAGE_2"}},
            {"type": "mystery", "secret": "CLAUDE_UNKNOWN"},
            {"type": "assistant", "sessionId": "s", "message": {"role": "assistant",
                "content": [{"type": "text", "text": "CLAUDE_FINAL"}]}},
            {"type": "user", "sessionId": "s", "message": {"role": "user", "content": "OUTSIDE_END"}},
        ]
        self.write_source()
        self.write_freeze(provider="claude")
        first = json.loads(self.call("--page", "1").stdout)
        second = json.loads(self.call("--page", "5").stdout)
        self.assertIn("CLAUDE_USER", json.dumps(first))
        self.assertIn("CLAUDE_FINAL", json.dumps(second))
        for hidden in ("CLAUDE_PRIVATE", "CLAUDE_UNKNOWN", "OUTSIDE_PAGE", "OUTSIDE_END"):
            self.assertNotIn(hidden, json.dumps(first) + json.dumps(second))
        self.assertEqual(first["omission_anchors"][0]["line"], 2)
        self.assertEqual(second["omission_anchors"][0]["line"], 5)

    def test_human_queued_command_anchor_is_explicit_and_page_scoped(self):
        self.records = [
            {"type": "queue-operation", "operation": "remove", "content": "Please check."},
            {"type": "attachment", "attachment": {"type": "queued_command",
                "prompt": "Please check.", "origin": {"kind": "human"}}},
            {"type": "attachment", "attachment": {"type": "queued_command",
                "prompt": "Automated prompt.", "origin": {"kind": "system"}}},
        ]
        self.write_source()
        self.write_freeze(provider="claude", physical_lines=3, page_starts=[1, 3])
        first = json.loads(self.call("--page", "1").stdout)
        last = json.loads(self.call("--page", "3").stdout)
        self.assertEqual(first["human_queued_command_lines"], [2])
        self.assertEqual(last["human_queued_command_lines"], [])
        self.assertEqual(json.loads(self.call("--line", "2").stdout)
                         ["human_queued_command_lines"], [2])

    def test_summary_inventories_long_visible_field_without_body(self):
        self.records[0]["payload"]["content"][0]["text"] = "VISIBLE_LONG_" * 400
        self.write_source()
        self.write_freeze()
        summary = json.loads(self.call("--summary", "1").stdout)
        self.assertEqual(summary["event_types"], {"message": 1})
        self.assertEqual(summary["long_fields"], [{
            "line": 1, "event_type": "message", "path": "$.content[0].text",
            "chars": 5200,
        }])
        self.assertNotIn("VISIBLE_LONG_", json.dumps(summary))
        self.assertNotIn("HIDDEN_REASONING", json.dumps(summary))
        self.assertNotIn("OUTSIDE_PAGE", json.dumps(summary))
        self.assertNotEqual(self.call("--summary", "3").returncode, 0)
        self.records[0]["payload"]["content"][0]["text"] = "CHANGED" * 1000
        self.write_source()
        rejected = self.call("--summary", "1")
        self.assertNotEqual(rejected.returncode, 0)
        self.assertEqual(rejected.stdout, "")

    def test_bounded_page_withholds_long_field_until_allowed_line_read(self):
        long_text = "VISIBLE_LONG_" * 400
        self.records[0]["payload"]["content"][0]["text"] = long_text
        self.write_source()
        self.write_freeze(bounded_page_char_limit=4000)
        summary = json.loads(self.call("--summary", "1").stdout)
        self.assertEqual(summary["long_fields"][0]["chars"], len(long_text))
        page = json.loads(self.call("--page", "1").stdout)
        self.assertEqual(page["events"][0]["content"][0]["text"],
                         {"omitted_long_field_chars": len(long_text)})
        self.assertNotIn("VISIBLE_LONG_", json.dumps(page))
        line = json.loads(self.call("--line", "1").stdout)
        self.assertEqual(line["events"][0]["content"][0]["text"], long_text)
        self.assertNotEqual(self.call("--line", "3").returncode, 0)

    def test_bounded_page_rejects_invalid_limit_and_redacts_long_gap_type(self):
        self.write_freeze(bounded_page_char_limit=0)
        self.assertNotEqual(self.call("--check").returncode, 0)
        self.records[0] = {"type": "UNKNOWN_SENTINEL" * 400, "payload": {"text": "HIDDEN_UNKNOWN"}}
        self.write_source()
        self.write_freeze(bounded_page_char_limit=4000)
        for action in ("--page", "--summary"):
            result = self.call(action, "1")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn("UNKNOWN_SENTINEL", result.stdout)
            self.assertNotIn("HIDDEN_UNKNOWN", result.stdout)


if __name__ == "__main__":
    unittest.main()
