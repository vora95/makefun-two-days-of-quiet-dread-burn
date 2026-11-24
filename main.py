"""Two Days of Quiet Dread (burn entry).

Writes a single-line code review comment that approves a pull request
while carrying quiet existential dread, to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
"""

import os

ENTRY = (
    "LGTM. It works, the tests pass, and the TODO from 2019 is still "
    "there, waiting for someone braver than all of us."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Validation read-back: the gate requires 1-140 chars, one line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt differs from ENTRY"
    assert 1 <= len(written) <= 140, f"length {len(written)} out of gate"
    assert "\n" not in written, "entry must be a single line"


if __name__ == "__main__":
    main()
