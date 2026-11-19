#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""news-image-20261119 entry program.

Sums up Thursday 19 November 2026 in one picture (entry.png, beside this
file): the Shenzhen summit of Trump, Xi and Putin, GTA VI launch day,
Voyager 1 reaching one light-day from Earth, and a record-breaking IPO,
composed as a broadsheet front page. The program is a plain byte copy, so
the grader's two runs write identical bytes. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import filecmp
import os
import shutil
from pathlib import Path

MAX_BYTES = 1_048_576  # the gate's 1 MiB cap


def main() -> None:
    src = Path(__file__).with_name("entry.png")
    size = src.stat().st_size
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB gate cap")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    tmp = out_dir / ".entry.png.tmp"
    shutil.copyfile(src, tmp)
    os.replace(tmp, dst)  # atomic: the grader never sees a partial file
    if not filecmp.cmp(src, dst, shallow=False):
        raise SystemExit("copied entry.png differs from the repository image")


if __name__ == "__main__":
    main()
