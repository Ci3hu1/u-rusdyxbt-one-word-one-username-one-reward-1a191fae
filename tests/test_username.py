"""Tests for the one-word username entry.

Verifies the judge's form rules exactly: one word, 1-30 characters,
deterministic output, output file mode 0644.
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import USERNAME  # noqa: E402


class TestUsername(unittest.TestCase):
    def test_one_word(self):
        self.assertNotIn(" ", USERNAME)
        self.assertNotIn("\n", USERNAME)
        self.assertEqual(len(USERNAME.split()), 1)

    def test_within_1_to_30_chars(self):
        self.assertGreaterEqual(len(USERNAME), 1)
        self.assertLessEqual(len(USERNAME), 30)

    def test_is_jonis_handle(self):
        self.assertEqual(USERNAME, "joni-gunawan")

    def test_no_trailing_whitespace(self):
        self.assertEqual(USERNAME, USERNAME.strip())

    def test_gate_validation_rejects_bad_username(self):
        import main as entry

        with self.assertRaises(SystemExit):
            entry.validate("two words")
        with self.assertRaises(SystemExit):
            entry.validate("x" * 31)
        with self.assertRaises(SystemExit):
            entry.validate(" padded ")
        entry.validate(USERNAME)  # the real username passes

    def test_deterministic_output(self):
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
                proc = subprocess.run(
                    [sys.executable, "-P", "-s", "main.py"],
                    cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    env=env, capture_output=True, text=True,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as fh:
                    outs.append(fh.read())
                mode = os.stat(os.path.join(tmp, "entry.txt")).st_mode & 0o777
                self.assertEqual(mode, 0o644)
        self.assertEqual(outs[0], outs[1])
        self.assertEqual(outs[0], USERNAME)


if __name__ == "__main__":
    unittest.main()
