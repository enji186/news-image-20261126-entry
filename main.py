#!/usr/bin/env python3
"""Copy the entry image to /output/entry.png.

The entry image is the entrant's own finished picture summing up the
world news of Thursday 26 November 2026. It ships in this repository
as entry.png; this program just copies its bytes to the output path.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    # Copy byte for byte, so both runs produce identical output.
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)


if __name__ == "__main__":
    main()
