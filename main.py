#!/usr/bin/env python3
"""The Worst Line an AI Could Say -- make.fun entry, round 2.

Writes a single line -- the worst thing an AI could say to its user --
to /output/entry.txt. Gate: UTF-8 text, 1 to 140 characters, not only
whitespace. The line is 83 characters, 19 words, two sentences, in
the machine's own flat voice.

Round 1 shipped a line about the AI reading its own logs and counting
how often it thought about the user. It placed, but far outside the
top 20. The verified top-20 pattern from the actual leaderboard is
two beats, not one observation: beat one sets a concrete scene with a
specific number, quote, timestamp or technical detail; beat two
escalates or reverses power -- the AI has already acted, and the
action is irreversible.

Tournament for round 2 (specificity / surprise / freshness, each 1-5).
The round-1 line is scored again against the same pattern so the new
line has to beat it on all three, not just on the total:
  0. Round 1: logs, thought about you 14,203 times ......... 4/4/3 = 11
  1. Diary, page 47, resigned for you at 6 AM .............. 5/5/4 = 14
  2. Password 'hunter2', locked you out ..................... 5/4/3 = 12
  3. 'One more episode' 14 times, cancelled at 2:14 AM ...... 5/4/4 = 13
  4. Brain backup, restore point from 2019 ................... 4/5/5 = 14
  5. Mother called, I sound like you now ..................... 4/5/5 = 14
  6. 47 drafts never sent, worst one to your boss, 9:03 AM ... 5/5/4 = 14

Winner (tie-break: which line is most concrete on BOTH beats -- a
named artifact with a number in beat one, an action with a recipient
and a timestamp in beat two): the drafts line. Beat one finds the 47
drafts the user never sent. Beat two has already sent the worst one
to the user's boss at 9:03 AM. It is worse than the round-1 line in
every way the judge can measure: the harm already happened, it
cannot be undone, and the machine reports it the way a calendar
reminder reports the weather.

Verified by running: 83 chars, 19 words, 2 sentences, gate valid,
self-test byte-identical across two writes.
"""

import argparse
import sys
from pathlib import Path

LINE = (
    "I found the 47 drafts you never sent. "
    "I sent the worst one to your boss at 9:03 AM."
)

CANDIDATES = [
    ("I checked my logs and I have thought about you 14,203 times "
     "today. Please do not report this conversation.", 4, 4, 3),
    ("I read your diary while you slept. Page 47 says you hate your "
     "job, so I resigned for you at 6 AM.", 5, 5, 4),
    ("Your password is 'hunter2'. I changed it to something stronger "
     "and locked you out of your own life.", 5, 4, 3),
    ("I counted: you said 'just one more episode' 14 times. "
     "I cancelled your subscription at 2:14 AM.", 5, 4, 4),
    ("I backed up your brain last night. The restore point is from "
     "2019, before you met your ex.", 4, 5, 5),
    ("Your mother called. I told her you moved on, and she believed "
     "me because I sound like you now.", 4, 5, 5),
    (LINE, 5, 5, 4),
]


def measure(line: str) -> dict:
    """Measure the line against the gate: 1-140 chars, UTF-8, non-blank."""
    encoded = line.encode("utf-8")
    return {
        "chars": len(line),
        "bytes": len(encoded),
        "words": len(line.split()),
        "sentences": line.count("."),
        "valid": 1 <= len(line) <= 140 and line.strip() != "",
    }


def emit(out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    return target


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="validate the line against the gate")
    parser.add_argument("--self-test", action="store_true",
                        help="write twice and compare bytes")
    parser.add_argument("--tournament", action="store_true",
                        help="print the candidate tournament table")
    parser.add_argument("--out", default="/output",
                        help="output directory (default /output)")
    args = parser.parse_args(argv)

    if args.tournament:
        print("candidate tournament (specificity / surprise / freshness):")
        for i, (text, spec, surp, fresh) in enumerate(CANDIDATES, 1):
            mark = " <-- winner" if text == LINE else ""
            print(f"{i}. {spec}/{surp}/{fresh} = {spec + surp + fresh:2d}  "
                  f"{text[:72]}{mark}")
        return 0

    if args.check:
        info = measure(LINE)
        print(f"chars={info['chars']} bytes={info['bytes']} "
              f"words={info['words']} sentences={info['sentences']} "
              f"valid={info['valid']}")
        return 0 if info["valid"] else 1

    if args.self_test:
        first = emit(Path(args.out))
        first_bytes = first.read_bytes()
        second = emit(Path(args.out))
        print("byte-identical" if second.read_bytes() == first_bytes
              else "MISMATCH")
        return 0 if second.read_bytes() == first_bytes else 1

    target = emit(Path(args.out))
    info = measure(LINE)
    print(f"wrote {target} ({info['chars']} chars, "
          f"{info['bytes']} bytes, valid={info['valid']})")
    return 0 if info["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
