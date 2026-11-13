# cutest-picture-01 entry, v2.0: "Kitten & Bunny" (kitten-bunny).
# Cream kitten in a daisy crown and mint scarf hugging a sleeping bunny.
# Copies the picture to /output/entry.png. Deterministic: byte copy, no
# network, no randomness — identical output on every run.
from os import makedirs, path
from os import environ
from shutil import copyfile

HERE = path.dirname(path.abspath(__file__))
SOURCE = path.join(HERE, "art.jpg")
OUTDIR = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST = path.join(OUTDIR, "entry.png")

makedirs(path.dirname(DEST), exist_ok=True)
copyfile(SOURCE, DEST)
