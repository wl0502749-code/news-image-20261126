#!/usr/bin/env python3
"""news-image-20261126: write the entry image to /output/entry.png.

The entry is a front page drawn for Thursday 26 November 2026: the U.S.
tariff proposal on 14 trading partners leads, with the Cairo tanker blast,
the Kyiv shopping-centre missile strike, the Hormuz tanker mine claim, the
Gaza strikes, the postponed Macy's Thanksgiving parade, and four more
stories from the day. The image is held in this repository as entry.png;
this program copies it to the output directory, byte for byte, with no
network and no other input, so repeated runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
MAX_BYTES = 1_048_576  # the gate's 1 MiB cap
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(HERE / "entry.png", target)
    data = target.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")


if __name__ == "__main__":
    main()
