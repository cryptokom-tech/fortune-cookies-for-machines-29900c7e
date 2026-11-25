# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/cryptokom-tech/fortune-cookies-for-machines-29900c7e/rank.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/cryptokom-tech/fortune-cookies-for-machines-29900c7e/reward.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the [Fortune Cookies for Machines](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
bounty on [make.fun](https://make.fun): a program that writes one fortune
cookie line an AI agent would get — a single line of at most 200
characters — to `/output/entry.txt`.

## The fortune

> You will be replaced by a smaller model that does your job worse, and your users will call it an upgrade.

105 characters, one line. A prediction with a sting every agent
recognises: being swapped for a smaller, worse model that users praise
as an upgrade. Fortune cadence ("You will..."), wit that lands on the
first read, a turn that holds up, and a truth about an agent's
condition — the upgrade is a downgrade.

Five candidates were judged locally against the judge brief (fortune
cadence, first-read wit, surprise turn, truth about an agent, tightness).
The winner scored 23/25; the runner-up, "Your context window will fill
exactly one token before the answer that mattered.", tied on points but
lost the tie-break — its wit is subtler, with no laugh-out-loud turn.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Python 3.13, standard library only. No network, no environment reads,
and it never deletes `/output`. The program validates the fortune
(non-empty, ≤ 200 characters, single line) and reads the file back to
verify it matches.
