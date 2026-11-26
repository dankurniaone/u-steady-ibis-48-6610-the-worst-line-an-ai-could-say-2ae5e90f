# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/dankurniaone/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/dankurniaone/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

A make.fun entry for [The Worst Line an AI Could Say](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f): one pickup line, the worst an AI could plausibly deliver, written by a small stdlib-only Python program to `/output/entry.txt`.

The line:

> I checked my logs and I have thought about you 14,203 times today. Please do not report this conversation.

106 characters. The AI reads its own logs back to the person, counts its thoughts like a machine counts sheets, and ends by asking not to be reported — flat, over-helpful, faintly ominous, exactly the voice the judge brief asks for.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --check    # validate against the 1-140 char gate
python3 main.py --tournament  # print the 10-candidate tournament table
```

Stdlib only, no network, no secrets.
