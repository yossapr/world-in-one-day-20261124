# world-in-one-day-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/yossapr/world-in-one-day-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/yossapr/world-in-one-day-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One front page that sums up the world's news of Tuesday 24 November 2026: three drawn lead scenes (Huawei convicted on 10 of 12 counts in Brooklyn, a Houthi drone hitting Riyadh's PIF tower, Asia's chip stocks soaring on Huang's return to Nvidia), eight illustrated stories from every region, a UTC timeline, a numbered world map, 22 briefs and a date check. Every story is sourced and marked by how sure the reporting is: official, confirmed, reported or claim. Entered in the make.fun bounty [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124).

![The front page](entry.png)

## How it is made

- `tools/edition.py` holds the stories, their places, times and sources.
- `tools/art.py` draws every scene as SVG shapes: no photographs, logos or outside images.
- `tools/build.py` lays the page out in HTML, draws the map from Natural Earth's public-domain 1:110m land polygons, photographs it with headless Edge or Chrome at 2x and saves a 1024 x 1024 PNG under 1 MiB.
- `main.py` copies `entry.png` to `/output/entry.png`, byte for byte, with no network.

## Run it

```sh
python main.py                 # writes /output/entry.png (OUTPUT_DIR overrides /output)
python tools/build.py          # rebuilds entry.png (needs Pillow and Edge or Chrome)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=abadhj4r&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
