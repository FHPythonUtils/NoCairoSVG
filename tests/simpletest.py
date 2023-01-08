"""Test script to convert svg to png, eps and pdf"""
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))


import nocairosvg

gInputFile = f"{THISDIR}/data/firefox.svg"


nocairosvg.svg2png(url=gInputFile, write_to="firefox.png")
nocairosvg.svg2eps(url=gInputFile, write_to="firefox.eps")
nocairosvg.svg2pdf(url=gInputFile, write_to="firefox.pdf")
