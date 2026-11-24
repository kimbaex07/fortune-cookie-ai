#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Reads the single fortune line from entry.txt beside this file,
validates it is 1..140 characters, and writes its exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output").

Pure Python standard library only.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "entry.txt")
    with open(source_path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if not text.strip():
        print("entry.txt must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 140:
        print(f"entry must be 1..140 characters, got {len(text)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
    os.chmod(out_path, 0o644)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
