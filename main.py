"""Fortune in a Pot — entry program.

Writes one original fortune for a houseplant to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is a fixed constant: no input, no network,
no randomness, so both grading runs produce byte-identical output.
Written with no trailing newline, as the gate counts characters.
The line is exactly 114 characters (ASCII only), inside the 1–120 gate.
The fortune is read as if meant for the plant on the windowsill: before the
month is out, its keeper will be caught talking to it again, and the plant
will grow a little taller just to listen.
"""

import os

LINE = "Before the month is out, you will catch your keeper talking to you again, and grow a little taller just to listen."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
