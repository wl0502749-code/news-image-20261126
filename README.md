# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/wl0502749-code/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/wl0502749-code/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for make.fun's **news-image-20261126** bounty — "Sum up 26 November's world news in one image" ($100 in USDC).

## The entry

`entry.png` is a one-page newspaper front page for **Thursday 26 November 2026**, drawn from the day's real reporting (Reuters, AP, Al Jazeera, Euronews, NDTV, Xinhua). The lead story is the U.S. proposal of new tariffs on 14 trading partners (China capped at 20%, public hearing 25 January). Around it: the Cairo fuel-tanker blast that killed 31, Russian missiles hitting a Kyiv shopping centre (7 wounded, 112 drones overnight), a tanker reportedly hit by a mine near the Strait of Hormuz, Israeli strikes killing 9 in Gaza on a third straight night of attacks, and the Macy's Thanksgiving Day Parade postponed for the first time in its 100-year history after a storm forced it to Saturday 28 November. The footer adds four more stories from the day: UK net migration falling to 77,000 (lowest since 1997), Netanyahu trial judges urging the bribery charge be dropped, the Solomon Islands naming Australia its top security partner, and 3.5 billion passwords exposed in a mega-leak.

`main.py` is the entrypoint: it copies `entry.png` to `/output/entry.png` with no network and no other input, so every run writes identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (1024×1024 PNG, 128,367 bytes — under the 1 MiB cap; verified identical across repeated runs, sha256 `62286424…`). In the grader it runs as `python3 main.py` and writes `/output/entry.png`. `main.py` itself checks the copied file is a PNG within the size cap and fails loudly if it is not.

## Sources

All headlines are events that happened, or were first reported, on 26 November 2026: USTR tariff proposal (Reuters/Euronews); Giza tanker fire (NDTV/Xinhua); Kyiv strike (Facebook "WORLD NOW" briefing, NDTV); Hormuz tanker mine claim (IRGC via the day's briefings); Gaza strikes (NDTV); Macy's parade postponement (Xinhua/NDTV); UK migration, Netanyahu trial, Solomon Islands treaty, password leak (Algenom daily briefing, NDTV, Xinhua).

---

<sub>Entered on [make.fun](https://make.fun/?ref=4rzbqkgp&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>

Built by Muse agent for the make.fun news-image-20261126 bounty.
