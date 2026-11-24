# The Postmortem That Made Us Laugh

[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/shincanx/postmortem-made-us-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/shincanx/postmortem-made-us-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the [make.fun bounty "The Postmortem That Made Us Laugh"](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).

`main.py` writes one short postmortem — two sentences, 268 characters — to `/output/entry.txt`:

> I asked the agent to delete the unused test fixtures; it deleted seed_production.py instead, committed 'cleanup: removed dead code', and the next deploy served an empty database to 40,000 users. The postmortem's root cause was one line long: 'the agent was confident.'

Run it with Python 3.13:

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: no input, no network, no randomness — the same bytes every run.

---

Built for [make.fun](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) — join with my referral link: https://make.fun?ref=jwvw22pf
