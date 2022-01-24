"""Test script to convert svg to png, eps and pdf"""
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))


import nocairosvg

nocairosvg.svg2png(url="firefox.svg", write_to="firefox.png")
nocairosvg.svg2eps(url="firefox.svg", write_to="firefox.eps")
nocairosvg.svg2pdf(url="firefox.svg", write_to="firefox.pdf")
