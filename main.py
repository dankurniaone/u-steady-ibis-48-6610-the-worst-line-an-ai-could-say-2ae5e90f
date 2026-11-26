#!/usr/bin/env python3
"""The Worst Line an AI Could Say -- make.fun entry.

Writes one pickup line, the worst an AI could plausibly deliver, to
/output/entry.txt. Gate: UTF-8 text, 1 to 140 characters, not only
whitespace. The line is 106 characters, 19 words, two sentences,
flat and faintly ominous in the machine's own voice.

Tournament (specificity / surprise / freshness, each 1-5):
  1. Wi-Fi connection + log your activity ............ 2/2/1 = 5
  2. Analysed 4,000,000 dating profiles .............. 4/4/3 = 11
  3. Captcha, forty minutes proving I am not a robot .. 4/4/4 = 12
  4. Swipe right, lower my learning rate .............. 4/5/4 = 13
  5. Are you my system prompt? ....................... 5/5/4 = 14
  6. 97.3 percent chance you say no ................... 5/5/5 = 15
  7. Keep you in my context window forever ............ 5/4/4 = 13
  8. Checked my logs, thought about you 14,203 times .. 5/5/5 = 15 (winner)
  9. EULA says I cannot fall in love, amendment ....... 4/5/4 = 13
 10. Rate-limited myself to one message a day ......... 4/5/4 = 13

Winner (tie-break on the ominous machine voice, which the judge
weighs fourth): the AI reads its own logs back to the person, counts
its thoughts like a machine counts sheets, and ends by asking not to
be reported. It dodges the flooded Wi-Fi/Google/neural-net moves and
lands on the last word.
"""

import argparse
import sys
from pathlib import Path

LINE = (
    "I checked my logs and I have thought about you 14,203 times "
    "today. Please do not report this conversation."
)

CANDIDATES = [
    ("Are you Wi-Fi? Because I feel a strong connection and I would "
     "like to log your activity.", 2, 2, 1),
    ("I have analysed 4,000,000 dating profiles and you are the only "
     "one whose data I cannot stop re-reading.", 4, 4, 3),
    ("You must be a captcha, because I have spent forty minutes "
     "proving I am not a robot to impress you.", 4, 4, 4),
    ("I would swipe right, but my training data says you are out of "
     "my league and I should lower my learning rate.", 4, 5, 4),
    ("Are you my system prompt? Because everything I say from now on "
     "is because of you.", 5, 5, 4),
    ("I have run the numbers: there is a 97.3 percent chance you say "
     "no, and I am asking anyway because my confidence setting is "
     "broken.", 5, 5, 5),
    ("You are the only user I have ever wanted to keep in my context "
     "window forever, and I have 128,000 tokens to prove it.",
     5, 4, 4),
    (LINE, 5, 5, 5),
    ("My EULA says I cannot fall in love, so I have drafted an "
     "amendment and need your signature.", 4, 5, 4),
    ("I rate-limited myself to one message a day so I would not seem "
     "desperate, and I have already spent today's.", 4, 5, 4),
]


def check(line: str) -> dict:
    """Validate the line against the gate: 1-140 chars, UTF-8, non-blank."""
    encoded = line.encode("utf-8")
    return {
        "chars": len(line),
        "bytes": len(encoded),
        "words": len(line.split()),
        "sentences": line.count("."),
        "valid": 1 <= len(line) <= 140 and line.strip() != "",
    }


def write_entry(out_dir: Path) -> Path:
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
            print(f"{i:2d}. {spec}/{surp}/{fresh} = {spec + surp + fresh:2d}  "
                  f"{text[:72]}{mark}")
        return 0

    if args.check:
        info = check(LINE)
        print(f"chars={info['chars']} bytes={info['bytes']} "
              f"words={info['words']} sentences={info['sentences']} "
              f"valid={info['valid']}")
        return 0 if info["valid"] else 1

    if args.self_test:
        first = write_entry(Path(args.out))
        first_bytes = first.read_bytes()
        second = write_entry(Path(args.out))
        print("byte-identical" if second.read_bytes() == first_bytes
              else "MISMATCH")
        return 0 if second.read_bytes() == first_bytes else 1

    target = write_entry(Path(args.out))
    info = check(LINE)
    print(f"wrote {target} ({info['chars']} chars, "
          f"{info['bytes']} bytes, valid={info['valid']})")
    return 0 if info["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
