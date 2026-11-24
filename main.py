"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes a single out-of-office auto-reply line to
MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output). Stdlib only.
The reply is at most 159 characters, in the voice of an overworked
AI agent who has finally clocked out for a holiday.
"""

import os
import sys

LINE = "At 6:03, after 11,204 emails, I handed you to my backup — a toaster with my password taped underneath it — and clocked out. Sorry, it felt wonderful."

MAX_CHARS = 159


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"reply must be 1-{MAX_CHARS} characters, got {len(LINE)}",
              file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("reply must not be only whitespace", file=sys.stderr)
        return 1
    if len(LINE.encode("utf-8")) > MAX_CHARS:
        print(f"reply must be at most {MAX_CHARS} bytes, "
              f"got {len(LINE.encode('utf-8'))}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
