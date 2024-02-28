"""Test script to convert svg to png, eps and pdf"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from imgcompare import imgcompare
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))


import nocairosvg

gInputFile = f"{THISDIR}/data/firefox.svg"


def getPdfData(pdf: str) -> str:
	return re.findall(
		r"\/Subtype \/Image(.*?)endstream",
		Path(pdf).read_text(encoding="utf-8", errors="ignore"),
		re.M | re.S,
	)[0]


def test_svg2png():
	"""test_svg2png"""
	outputFile = f"{THISDIR}/data/firefox.png"
	nocairosvg.svg2png(url=gInputFile, write_to=outputFile)
	output = Image.open(outputFile)
	expected = Image.open(f"{THISDIR}/data/firefox_expected.png")
	assert imgcompare.is_equal(
		output,
		expected,
		tolerance=0.2,
	)


def test_svg2eps():
	"""test_svg2eps"""
	outputFile = f"{THISDIR}/data/firefox.eps"
	nocairosvg.svg2eps(url=gInputFile, write_to=outputFile)
	assert (
		Path(outputFile).read_bytes()
		== Path(f"{THISDIR}/data/firefox_expected.eps").read_bytes()
	)


def test_svg2pdf():
	"""test_svg2pdf"""
	outputFile = f"{THISDIR}/data/firefox.pdf"
	nocairosvg.svg2pdf(url=gInputFile, write_to=outputFile)
	assert getPdfData(outputFile) == getPdfData(f"{THISDIR}/data/firefox_expected.pdf")


if __name__ == "__main__":
	test_svg2png()
	test_svg2eps()
	test_svg2pdf()
