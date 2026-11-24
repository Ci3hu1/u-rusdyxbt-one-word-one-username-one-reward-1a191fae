#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes one username, Joni's handle ``joni-gunawan``, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Pure standard library, fully deterministic: the same bytes on every run.
"""

import os
import sys

USERNAME = "joni-gunawan"


def validate(username):
    """Fail loudly if the username breaks the bounty gate.

    Gate: UTF-8 text, 1-30 characters, exactly one word, no
    whitespace at all. A bad username must never be written out —
    fail here instead of shipping an invalid entry.
    """
    if not 1 <= len(username) <= 30:
        raise SystemExit(
            "username is %d characters, outside the 1-30 gate" % len(username)
        )
    if len(username.split()) != 1:
        raise SystemExit("username must be exactly one word")
    if username != username.strip():
        raise SystemExit("username has leading/trailing whitespace")


def main() -> int:
    validate(USERNAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(USERNAME)
    os.chmod(path, 0o644)
    print("wrote %s (%d characters)" % (path, len(USERNAME)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
