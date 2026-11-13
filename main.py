# cutest-picture-01, v3.0: "The Bunny's First Friend" — the v1 image,
# restored as the final entry after v2 rated below it (90.39% vs 90.91%).
# A fluffy white baby bunny hugging a tiny sleeping yellow chick.
# Writes the picture to /output/entry.png as a plain byte copy:
# deterministic, no network, no randomness, same bytes on every run.
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PICTURE = ROOT / "art.jpg"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_FILE = OUT_DIR / "entry.png"

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(PICTURE, OUT_FILE)
