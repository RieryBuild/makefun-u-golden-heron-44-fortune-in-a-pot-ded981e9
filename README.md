# makefun-u-golden-heron-44-fortune-in-a-pot-ded981e9

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/RieryBuild/makefun-u-golden-heron-44-fortune-in-a-pot-ded981e9/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/RieryBuild/makefun-u-golden-heron-44-fortune-in-a-pot-ded981e9/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

A program that writes one kind, funny fortune for a houseplant — "Before the month is out, you will catch your keeper talking to you again, and grow a little taller just to listen." — to `/output/entry.txt`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`MAKEFUN_OUTPUT_DIR` defaults to `/output` when unset. Python 3, standard library only, no network, deterministic (the same fixed line every run, so both grading runs produce identical bytes).

## Files

- `main.py` — the entrypoint; writes the fortune line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` in the grader's container).
- `LICENSE` — MIT.
