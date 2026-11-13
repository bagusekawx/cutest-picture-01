# cutest-picture-01 entry: "The Bunny's First Friend".
# v1.0 — white bunny in a pink scarf hugging a sleeping chick.
# Writes the picture to /output/entry.png with a plain byte copy.
# Deterministic: no network, no randomness, same bytes every run.
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(BASE, "art.jpg")
TARGET = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(TARGET), exist_ok=True)
shutil.copyfile(IMAGE, TARGET)
