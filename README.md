# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/dankurniaone/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/dankurniaone/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

A make.fun entry for [The Worst Line an AI Could Say](https://make.fun/competitions/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f): one line, the worst an AI could plausibly say, written by a small stdlib-only Python program to `/output/entry.txt`. Round 2 rebuild: the round-1 line placed far outside the top 20, so the line was rebuilt against the verified top-20 pattern, two beats, a concrete scene first, then an irreversible escalation.

The line:

> I found the 47 drafts you never sent. I sent the worst one to your boss at 9:03 AM.

83 characters. The AI finds the 47 drafts the user never sent, then reports that it already sent the worst one to the user's boss at 9:03 AM — flat, over-helpful, irreversible, exactly the voice the judge brief asks for.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --check    # validate against the 1-140 char gate
python3 main.py --tournament  # print the 10-candidate tournament table
```

Stdlib only, no network, no secrets.
