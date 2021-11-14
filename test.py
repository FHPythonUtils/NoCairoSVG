"""Test script to convert svg to png, eps and pdf"""

from __future__ import annotations

import nocairosvg

nocairosvg.svg2png(url="firefox.svg", write_to="firefox.png")
nocairosvg.svg2eps(url="firefox.svg", write_to="firefox.eps")
nocairosvg.svg2pdf(url="firefox.svg", write_to="firefox.pdf")
