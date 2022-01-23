"""NoCairoSVG - A simple SVG converter not based on Cairo! (Uses pyppeteer)
"""

from __future__ import annotations

import asyncio
import base64
import os
from io import BytesIO, FileIO
from pathlib import Path

from PIL import Image, ImageOps
from pyppeteer import launch

THISDIR = str(Path(__file__).resolve().parent)


def svg2svg(
	bytestring: bytes | None = None,
	file_obj: FileIO | None = None,
	url: str | None = None,
	dpi: int = 96,
	parent_width: int | None = None,
	parent_height: int | None = None,
	scale: float = 1,
	unsafe: bool = False,
	background_color: str | None = None,
	negate_colors: bool = False,
	invert_images: bool = False,
	write_to: str | FileIO | None = None,
	output_width: int | None = None,
	output_height: int | None = None,
) -> bytes | None:
	"""Convert an SVG to an SVG

	Args:
		bytestring (Optional[bytes], optional): bytes containing svg data. Defaults to None.
		file_obj (Optional[FileIO], optional): opened file object. Defaults to None.
		url (Optional[str], optional): path to file. Defaults to None.
		dpi (int, optional): dpi. Defaults to 96.
		parent_width (Optional[int], optional): width of the parent element
		(e.g. div). Defaults to None.
		parent_height (Optional[int], optional): height of the parent element
		(e.g. div). Defaults to None.
		scale (float, optional): scale the image by . Defaults to 1.
		unsafe (bool, optional): NA here . Defaults to False.
		background_color (Optional[str], optional): Set a bg colour if not
		transparent. Defaults to None.
		negate_colors (bool, optional): invert the image colours. Defaults to False.
		invert_images (bool, optional): invert the image colours. Defaults to False.
		write_to (Union[str, FileIO, None], optional): file path/ object to
		write to (Omit to return bytes). Defaults to None.
		output_width (Optional[int], optional): width of output image. Defaults to None.
		output_height (Optional[int], optional): height of output image.
		Defaults to None.

	Returns:
		Optional[bytes]: Bytes of image if write_to is None. else writes image
		to file
	"""
	raise NotImplementedError


def svg2png(
	bytestring: bytes | None = None,
	file_obj: FileIO | None = None,
	url: str | None = None,
	dpi: int = 96,
	parent_width: int | None = None,
	parent_height: int | None = None,
	scale: float = 1,
	unsafe: bool = False,
	background_color: str | None = None,
	negate_colors: bool = False,
	invert_images: bool = False,
	write_to: str | FileIO | None = None,
	output_width: int | None = None,
	output_height: int | None = None,
) -> bytes | None:
	"""Convert an SVG to a PNG

	Args:
		bytestring (Optional[bytes], optional): bytes containing svg data. Defaults to None.
		file_obj (Optional[FileIO], optional): opened file object. Defaults to None.
		url (Optional[str], optional): path to file. Defaults to None.
		dpi (int, optional): dpi. Defaults to 96.
		parent_width (Optional[int], optional): width of the parent element
		(e.g. div). Defaults to None.
		parent_height (Optional[int], optional): height of the parent element
		(e.g. div). Defaults to None.
		scale (float, optional): scale the image by . Defaults to 1.
		unsafe (bool, optional): NA here . Defaults to False.
		background_color (Optional[str], optional): Set a bg colour if not
		transparent. Defaults to None.
		negate_colors (bool, optional): invert the image colours. Defaults to False.
		invert_images (bool, optional): invert the image colours. Defaults to False.
		write_to (Union[str, FileIO, None], optional): file path/ object to
		write to (Omit to return bytes). Defaults to None.
		output_width (Optional[int], optional): width of output image. Defaults to None.
		output_height (Optional[int], optional): height of output image.
		Defaults to None.

	Returns:
		Optional[bytes]: Bytes of image if write_to is None. else writes image
		to file
	"""
	del unsafe
	return svg2bitmap(
		bytestring,
		file_obj,
		url,
		dpi,
		parent_width,
		parent_height,
		scale,
		background_color,
		negate_colors,
		invert_images,
		write_to,
		output_width,
		output_height,
		"png",
	)


def svg2pdf(
	bytestring: bytes | None = None,
	file_obj: FileIO | None = None,
	url: str | None = None,
	dpi: int = 96,
	parent_width: int | None = None,
	parent_height: int | None = None,
	scale: float = 1,
	unsafe: bool = False,
	background_color: str | None = None,
	negate_colors: bool = False,
	invert_images: bool = False,
	write_to: str | FileIO | None = None,
	output_width: int | None = None,
	output_height: int | None = None,
) -> bytes | None:
	"""Convert an SVG to a PDF

	Args:
		bytestring (Optional[bytes], optional): bytes containing svg data. Defaults to None.
		file_obj (Optional[FileIO], optional): opened file object. Defaults to None.
		url (Optional[str], optional): path to file. Defaults to None.
		dpi (int, optional): dpi. Defaults to 96.
		parent_width (Optional[int], optional): width of the parent element
		(e.g. div). Defaults to None.
		parent_height (Optional[int], optional): height of the parent element
		(e.g. div). Defaults to None.
		scale (float, optional): scale the image by . Defaults to 1.
		unsafe (bool, optional): NA here . Defaults to False.
		background_color (Optional[str], optional): Set a bg colour if not
		transparent. Defaults to None.
		negate_colors (bool, optional): invert the image colours. Defaults to False.
		invert_images (bool, optional): invert the image colours. Defaults to False.
		write_to (Union[str, FileIO, None], optional): file path/ object to
		write to (Omit to return bytes). Defaults to None.
		output_width (Optional[int], optional): width of output image. Defaults to None.
		output_height (Optional[int], optional): height of output image.
		Defaults to None.

	Returns:
		Optional[bytes]: Bytes of image if write_to is None. else writes image
		to file
	"""
	del unsafe
	return svg2bitmap(
		bytestring,
		file_obj,
		url,
		dpi,
		parent_width,
		parent_height,
		scale,
		"white" if background_color is None else background_color,
		negate_colors,
		invert_images,
		write_to,
		output_width,
		output_height,
		"pdf",
		False,
	)


def svg2ps(
	bytestring: bytes | None = None,
	file_obj: FileIO | None = None,
	url: str | None = None,
	dpi: int = 96,
	parent_width: int | None = None,
	parent_height: int | None = None,
	scale: float = 1,
	unsafe: bool = False,
	background_color: str | None = None,
	negate_colors: bool = False,
	invert_images: bool = False,
	write_to: str | FileIO | None = None,
	output_width: int | None = None,
	output_height: int | None = None,
) -> bytes | None:
	"""Convert an SVG to PS

	Args:
		bytestring (Optional[bytes], optional): bytes containing svg data. Defaults to None.
		file_obj (Optional[FileIO], optional): opened file object. Defaults to None.
		url (Optional[str], optional): path to file. Defaults to None.
		dpi (int, optional): dpi. Defaults to 96.
		parent_width (Optional[int], optional): width of the parent element
		(e.g. div). Defaults to None.
		parent_height (Optional[int], optional): height of the parent element
		(e.g. div). Defaults to None.
		scale (float, optional): scale the image by . Defaults to 1.
		unsafe (bool, optional): NA here . Defaults to False.
		background_color (Optional[str], optional): Set a bg colour if not
		transparent. Defaults to None.
		negate_colors (bool, optional): invert the image colours. Defaults to False.
		invert_images (bool, optional): invert the image colours. Defaults to False.
		write_to (Union[str, FileIO, None], optional): file path/ object to
		write to (Omit to return bytes). Defaults to None.
		output_width (Optional[int], optional): width of output image. Defaults to None.
		output_height (Optional[int], optional): height of output image.
		Defaults to None.

	Returns:
		Optional[bytes]: Bytes of image if write_to is None. else writes image
		to file
	"""
	raise NotImplementedError


def svg2eps(
	bytestring: bytes | None = None,
	file_obj: FileIO | None = None,
	url: str | None = None,
	dpi: int = 96,
	parent_width: int | None = None,
	parent_height: int | None = None,
	scale: float = 1,
	unsafe: bool = False,
	background_color: str | None = None,
	negate_colors: bool = False,
	invert_images: bool = False,
	write_to: str | FileIO | None = None,
	output_width: int | None = None,
	output_height: int | None = None,
) -> bytes | None:
	"""Convert an SVG to EPS

	Args:
		bytestring (Optional[bytes], optional): bytes containing svg data. Defaults to None.
		file_obj (Optional[FileIO], optional): opened file object. Defaults to None.
		url (Optional[str], optional): path to file. Defaults to None.
		dpi (int, optional): dpi. Defaults to 96.
		parent_width (Optional[int], optional): width of the parent element
		(e.g. div). Defaults to None.
		parent_height (Optional[int], optional): height of the parent element
		(e.g. div). Defaults to None.
		scale (float, optional): scale the image by . Defaults to 1.
		unsafe (bool, optional): NA here . Defaults to False.
		background_color (Optional[str], optional): Set a bg colour if not
		transparent. Defaults to None.
		negate_colors (bool, optional): invert the image colours. Defaults to False.
		invert_images (bool, optional): invert the image colours. Defaults to False.
		write_to (Union[str, FileIO, None], optional): file path/ object to
		write to (Omit to return bytes). Defaults to None.
		output_width (Optional[int], optional): width of output image. Defaults to None.
		output_height (Optional[int], optional): height of output image.
		Defaults to None.

	Returns:
		Optional[bytes]: Bytes of image if write_to is None. else writes image
		to file
	"""
	del unsafe
	return svg2bitmap(
		bytestring,
		file_obj,
		url,
		dpi,
		parent_width,
		parent_height,
		scale,
		"white" if background_color is None else background_color,
		negate_colors,
		invert_images,
		write_to,
		output_width,
		output_height,
		"eps",
		False,
	)


def svg2bitmap(
	bytestring: bytes | None = None,
	file_obj: FileIO | None = None,
	url: str | None = None,
	dpi: int = 96,
	parent_width: int | None = None,
	parent_height: int | None = None,
	scale: float = 1,
	background_color: str | None = None,
	negate_colors: bool = False,
	invert_images: bool = False,
	write_to: str | FileIO | None = None,
	output_width: int | None = None,
	output_height: int | None = None,
	ext: str = "png",
	transparent: bool = True,
) -> bytes | None:
	"""Convert an SVG to an SVG

	Args:
		bytestring (Optional[bytes], optional): bytes containing svg data. Defaults to None.
		file_obj (Optional[FileIO], optional): opened file object. Defaults to None.
		url (Optional[str], optional): path to file. Defaults to None.
		dpi (int, optional): dpi. Defaults to 96.
		parent_width (Optional[int], optional): width of the parent element
		(e.g. div). Defaults to None.
		parent_height (Optional[int], optional): height of the parent element
		(e.g. div). Defaults to None.
		scale (float, optional): scale the image by . Defaults to 1.
		background_color (Optional[str], optional): Set a bg colour if not
		transparent. Defaults to None.
		negate_colors (bool, optional): invert the image colours. Defaults to False.
		invert_images (bool, optional): invert the image colours. Defaults to False.
		write_to (Union[str, FileIO, None], optional): file path/ object to
		write to (Omit to return bytes). Defaults to None.
		output_width (Optional[int], optional): width of output image. Defaults to None.
		output_height (Optional[int], optional): height of output image.
		Defaults to None.
		ext (str): image type. Defaults to 'png'
		transparent (bool): Should the image be transparent. Defaults to True

	Returns:
		Optional[bytes]: Bytes of image if write_to is None. else writes image
		to file
	"""
	# Render the SVG
	url = "file:///" + os.path.abspath(url).replace("\\", "/") if url is not None else None
	image = asyncio.get_event_loop().run_until_complete(
		convert(
			resolve_file_url(bytestring, file_obj, url),
			colour2tuple(background_color) if background_color is not None else (0, 0, 0, 0),
			(parent_width, parent_height),
		)
	)
	new_width = output_width if output_width is not None else int(image.width * scale)
	new_height = output_height if output_height is not None else int(image.height * scale)
	# Apply scale/ set output width and height
	image.resize((new_width, new_height), Image.ANTIALIAS)
	# Invert images
	if invert_images or negate_colors:
		image = ImageOps.invert(image)
	# If opaque
	if not transparent:
		image = image.convert("RGB")
	return write(image, write_to, ext, dpi)


def resolve_file_url(
	bytestring: bytes | None = None, file_obj: FileIO | None = None, url: str | None = None
) -> str:
	"""Get a file url from a bytestring, file object, or url...

	Args:
		bytestring (Optional[bytes], optional): svg bytes. Defaults to None.
		file_obj (Optional[FileIO], optional): file object. Defaults to None.
		url (Optional[str], optional): path. Defaults to None.

	Returns:
		str: path
	"""
	if url is not None:
		return url
	if file_obj is not None:
		file_name = getattr(file_obj, "name", None)
		if file_name is not None:
			return file_name

		Path(f"{THISDIR}/temp.svg").write_bytes(file_obj.read())
		return f"{THISDIR}/temp.svg"
	if bytestring is not None:
		Path(f"{THISDIR}/temp.svg").write_bytes(bytestring)
		return f"{THISDIR}/temp.svg"
	return "err"


def write(image: Image.Image, file: str | FileIO | None, ext: str, dpi: int) -> bytes | None:
	"""Write the pil image to the filesystem

	Args:
		image (Image.Image): pillow image
		file (Union[str, FileIO, None]): the file
		ext (str): the image extension
		dpi (int): the dpi

	Returns:
		Optional[bytes]: the image data in bytes if no file specified
	"""
	if file is not None:
		image.save(file, format=ext, dpi=(dpi, dpi))
		return None
	image.save(THISDIR + "/temp.svg", format=ext, dpi=(dpi, dpi))
	return open(THISDIR + "/temp.svg", "rb").read()


async def convert(
	url: str,
	background_colour: tuple[int, int, int, int] = (0, 0, 0, 0),
	size: tuple[int | None, int | None] = (None, None),
) -> Image.Image:
	"""Launch pyppeteer and use the html canvas to convert

	Args:
		url (str): location of the image to convert
		background_colour (Tuple[int, int, int, int], optional): Set the background colour.
		Defaults to (0, 0, 0, 0).
		size (Tuple[Optional[int], Optional[int]], optional): Size to crop the image to.
		Defaults to (None, None).

	Returns:
		Image.Image: PIL Image
	"""
	browser = await launch(
		options={
			"args": ["--no-sandbox", "--disable-web-security", "--allow-file-access-from-files"]
		}
	)
	page = await browser.newPage()
	await page.setViewport({"width": 4000, "height": 4000})
	await page.goto("file:///" + THISDIR + "/convert.html")
	width = "0" if size[0] is None else str(size[0]) + "px"
	height = "0" if size[1] is None else str(size[1]) + "px"
	await page.evaluate(f"convert('{width}', '{height}', 'rgb{background_colour}', '{url}')")
	await page.waitForSelector("div")
	png_dat = await page.evaluate("document.getElementById('div1').innerText")
	png_dat = png_dat[22:]  # data:image/png;base64,
	img = Image.open(BytesIO(base64.b64decode(png_dat)))
	return img


def colour2tuple(colour: str | None) -> tuple[int, int, int, int]:
	"""Convert a colour string to tuple

	Args:
		colour (Optional[str]): the colour

	Returns:
		Tuple[int, int, int, int]: the converted colour
	"""
	colours = {
		"aliceblue": (240 / 255, 248 / 255, 255 / 255, 1),
		"antiquewhite": (250 / 255, 235 / 255, 215 / 255, 1),
		"aqua": (0 / 255, 255 / 255, 255 / 255, 1),
		"aquamarine": (127 / 255, 255 / 255, 212 / 255, 1),
		"azure": (240 / 255, 255 / 255, 255 / 255, 1),
		"beige": (245 / 255, 245 / 255, 220 / 255, 1),
		"bisque": (255 / 255, 228 / 255, 196 / 255, 1),
		"black": (0 / 255, 0 / 255, 0 / 255, 1),
		"blanchedalmond": (255 / 255, 235 / 255, 205 / 255, 1),
		"blue": (0 / 255, 0 / 255, 255 / 255, 1),
		"blueviolet": (138 / 255, 43 / 255, 226 / 255, 1),
		"brown": (165 / 255, 42 / 255, 42 / 255, 1),
		"burlywood": (222 / 255, 184 / 255, 135 / 255, 1),
		"cadetblue": (95 / 255, 158 / 255, 160 / 255, 1),
		"chartreuse": (127 / 255, 255 / 255, 0 / 255, 1),
		"chocolate": (210 / 255, 105 / 255, 30 / 255, 1),
		"coral": (255 / 255, 127 / 255, 80 / 255, 1),
		"cornflowerblue": (100 / 255, 149 / 255, 237 / 255, 1),
		"cornsilk": (255 / 255, 248 / 255, 220 / 255, 1),
		"crimson": (220 / 255, 20 / 255, 60 / 255, 1),
		"cyan": (0 / 255, 255 / 255, 255 / 255, 1),
		"darkblue": (0 / 255, 0 / 255, 139 / 255, 1),
		"darkcyan": (0 / 255, 139 / 255, 139 / 255, 1),
		"darkgoldenrod": (184 / 255, 134 / 255, 11 / 255, 1),
		"darkgray": (169 / 255, 169 / 255, 169 / 255, 1),
		"darkgreen": (0 / 255, 100 / 255, 0 / 255, 1),
		"darkgrey": (169 / 255, 169 / 255, 169 / 255, 1),
		"darkkhaki": (189 / 255, 183 / 255, 107 / 255, 1),
		"darkmagenta": (139 / 255, 0 / 255, 139 / 255, 1),
		"darkolivegreen": (85 / 255, 107 / 255, 47 / 255, 1),
		"darkorange": (255 / 255, 140 / 255, 0 / 255, 1),
		"darkorchid": (153 / 255, 50 / 255, 204 / 255, 1),
		"darkred": (139 / 255, 0 / 255, 0 / 255, 1),
		"darksalmon": (233 / 255, 150 / 255, 122 / 255, 1),
		"darkseagreen": (143 / 255, 188 / 255, 143 / 255, 1),
		"darkslateblue": (72 / 255, 61 / 255, 139 / 255, 1),
		"darkslategray": (47 / 255, 79 / 255, 79 / 255, 1),
		"darkslategrey": (47 / 255, 79 / 255, 79 / 255, 1),
		"darkturquoise": (0 / 255, 206 / 255, 209 / 255, 1),
		"darkviolet": (148 / 255, 0 / 255, 211 / 255, 1),
		"deeppink": (255 / 255, 20 / 255, 147 / 255, 1),
		"deepskyblue": (0 / 255, 191 / 255, 255 / 255, 1),
		"dimgray": (105 / 255, 105 / 255, 105 / 255, 1),
		"dimgrey": (105 / 255, 105 / 255, 105 / 255, 1),
		"dodgerblue": (30 / 255, 144 / 255, 255 / 255, 1),
		"firebrick": (178 / 255, 34 / 255, 34 / 255, 1),
		"floralwhite": (255 / 255, 250 / 255, 240 / 255, 1),
		"forestgreen": (34 / 255, 139 / 255, 34 / 255, 1),
		"fuchsia": (255 / 255, 0 / 255, 255 / 255, 1),
		"gainsboro": (220 / 255, 220 / 255, 220 / 255, 1),
		"ghostwhite": (248 / 255, 248 / 255, 255 / 255, 1),
		"gold": (255 / 255, 215 / 255, 0 / 255, 1),
		"goldenrod": (218 / 255, 165 / 255, 32 / 255, 1),
		"gray": (128 / 255, 128 / 255, 128 / 255, 1),
		"grey": (128 / 255, 128 / 255, 128 / 255, 1),
		"green": (0 / 255, 128 / 255, 0 / 255, 1),
		"greenyellow": (173 / 255, 255 / 255, 47 / 255, 1),
		"honeydew": (240 / 255, 255 / 255, 240 / 255, 1),
		"hotpink": (255 / 255, 105 / 255, 180 / 255, 1),
		"indianred": (205 / 255, 92 / 255, 92 / 255, 1),
		"indigo": (75 / 255, 0 / 255, 130 / 255, 1),
		"ivory": (255 / 255, 255 / 255, 240 / 255, 1),
		"khaki": (240 / 255, 230 / 255, 140 / 255, 1),
		"lavender": (230 / 255, 230 / 255, 250 / 255, 1),
		"lavenderblush": (255 / 255, 240 / 255, 245 / 255, 1),
		"lawngreen": (124 / 255, 252 / 255, 0 / 255, 1),
		"lemonchiffon": (255 / 255, 250 / 255, 205 / 255, 1),
		"lightblue": (173 / 255, 216 / 255, 230 / 255, 1),
		"lightcoral": (240 / 255, 128 / 255, 128 / 255, 1),
		"lightcyan": (224 / 255, 255 / 255, 255 / 255, 1),
		"lightgoldenrodyellow": (250 / 255, 250 / 255, 210 / 255, 1),
		"lightgray": (211 / 255, 211 / 255, 211 / 255, 1),
		"lightgreen": (144 / 255, 238 / 255, 144 / 255, 1),
		"lightgrey": (211 / 255, 211 / 255, 211 / 255, 1),
		"lightpink": (255 / 255, 182 / 255, 193 / 255, 1),
		"lightsalmon": (255 / 255, 160 / 255, 122 / 255, 1),
		"lightseagreen": (32 / 255, 178 / 255, 170 / 255, 1),
		"lightskyblue": (135 / 255, 206 / 255, 250 / 255, 1),
		"lightslategray": (119 / 255, 136 / 255, 153 / 255, 1),
		"lightslategrey": (119 / 255, 136 / 255, 153 / 255, 1),
		"lightsteelblue": (176 / 255, 196 / 255, 222 / 255, 1),
		"lightyellow": (255 / 255, 255 / 255, 224 / 255, 1),
		"lime": (0 / 255, 255 / 255, 0 / 255, 1),
		"limegreen": (50 / 255, 205 / 255, 50 / 255, 1),
		"linen": (250 / 255, 240 / 255, 230 / 255, 1),
		"magenta": (255 / 255, 0 / 255, 255 / 255, 1),
		"maroon": (128 / 255, 0 / 255, 0 / 255, 1),
		"mediumaquamarine": (102 / 255, 205 / 255, 170 / 255, 1),
		"mediumblue": (0 / 255, 0 / 255, 205 / 255, 1),
		"mediumorchid": (186 / 255, 85 / 255, 211 / 255, 1),
		"mediumpurple": (147 / 255, 112 / 255, 219 / 255, 1),
		"mediumseagreen": (60 / 255, 179 / 255, 113 / 255, 1),
		"mediumslateblue": (123 / 255, 104 / 255, 238 / 255, 1),
		"mediumspringgreen": (0 / 255, 250 / 255, 154 / 255, 1),
		"mediumturquoise": (72 / 255, 209 / 255, 204 / 255, 1),
		"mediumvioletred": (199 / 255, 21 / 255, 133 / 255, 1),
		"midnightblue": (25 / 255, 25 / 255, 112 / 255, 1),
		"mintcream": (245 / 255, 255 / 255, 250 / 255, 1),
		"mistyrose": (255 / 255, 228 / 255, 225 / 255, 1),
		"moccasin": (255 / 255, 228 / 255, 181 / 255, 1),
		"navajowhite": (255 / 255, 222 / 255, 173 / 255, 1),
		"navy": (0 / 255, 0 / 255, 128 / 255, 1),
		"oldlace": (253 / 255, 245 / 255, 230 / 255, 1),
		"olive": (128 / 255, 128 / 255, 0 / 255, 1),
		"olivedrab": (107 / 255, 142 / 255, 35 / 255, 1),
		"orange": (255 / 255, 165 / 255, 0 / 255, 1),
		"orangered": (255 / 255, 69 / 255, 0 / 255, 1),
		"orchid": (218 / 255, 112 / 255, 214 / 255, 1),
		"palegoldenrod": (238 / 255, 232 / 255, 170 / 255, 1),
		"palegreen": (152 / 255, 251 / 255, 152 / 255, 1),
		"paleturquoise": (175 / 255, 238 / 255, 238 / 255, 1),
		"palevioletred": (219 / 255, 112 / 255, 147 / 255, 1),
		"papayawhip": (255 / 255, 239 / 255, 213 / 255, 1),
		"peachpuff": (255 / 255, 218 / 255, 185 / 255, 1),
		"peru": (205 / 255, 133 / 255, 63 / 255, 1),
		"pink": (255 / 255, 192 / 255, 203 / 255, 1),
		"plum": (221 / 255, 160 / 255, 221 / 255, 1),
		"powderblue": (176 / 255, 224 / 255, 230 / 255, 1),
		"purple": (128 / 255, 0 / 255, 128 / 255, 1),
		"red": (255 / 255, 0 / 255, 0 / 255, 1),
		"rosybrown": (188 / 255, 143 / 255, 143 / 255, 1),
		"royalblue": (65 / 255, 105 / 255, 225 / 255, 1),
		"saddlebrown": (139 / 255, 69 / 255, 19 / 255, 1),
		"salmon": (250 / 255, 128 / 255, 114 / 255, 1),
		"sandybrown": (244 / 255, 164 / 255, 96 / 255, 1),
		"seagreen": (46 / 255, 139 / 255, 87 / 255, 1),
		"seashell": (255 / 255, 245 / 255, 238 / 255, 1),
		"sienna": (160 / 255, 82 / 255, 45 / 255, 1),
		"silver": (192 / 255, 192 / 255, 192 / 255, 1),
		"skyblue": (135 / 255, 206 / 255, 235 / 255, 1),
		"slateblue": (106 / 255, 90 / 255, 205 / 255, 1),
		"slategray": (112 / 255, 128 / 255, 144 / 255, 1),
		"slategrey": (112 / 255, 128 / 255, 144 / 255, 1),
		"snow": (255 / 255, 250 / 255, 250 / 255, 1),
		"springgreen": (0 / 255, 255 / 255, 127 / 255, 1),
		"steelblue": (70 / 255, 130 / 255, 180 / 255, 1),
		"tan": (210 / 255, 180 / 255, 140 / 255, 1),
		"teal": (0 / 255, 128 / 255, 128 / 255, 1),
		"thistle": (216 / 255, 191 / 255, 216 / 255, 1),
		"tomato": (255 / 255, 99 / 255, 71 / 255, 1),
		"turquoise": (64 / 255, 224 / 255, 208 / 255, 1),
		"violet": (238 / 255, 130 / 255, 238 / 255, 1),
		"wheat": (245 / 255, 222 / 255, 179 / 255, 1),
		"white": (255 / 255, 255 / 255, 255 / 255, 1),
		"whitesmoke": (245 / 255, 245 / 255, 245 / 255, 1),
		"yellow": (255 / 255, 255 / 255, 0 / 255, 1),
		"yellowgreen": (154 / 255, 205 / 255, 50 / 255, 1),
		"activeborder": (0, 0, 1, 1),
		"activecaption": (0, 0, 1, 1),
		"appworkspace": (1, 1, 1, 1),
		"background": (1, 1, 1, 1),
		"buttonface": (0, 0, 0, 1),
		"buttonhighlight": (0.8, 0.8, 0.8, 1),
		"buttonshadow": (0.2, 0.2, 0.2, 1),
		"buttontext": (0, 0, 0, 1),
		"captiontext": (0, 0, 0, 1),
		"graytext": (0.2, 0.2, 0.2, 1),
		"highlight": (0, 0, 1, 1),
		"highlighttext": (0.8, 0.8, 0.8, 1),
		"inactiveborder": (0.2, 0.2, 0.2, 1),
		"inactivecaption": (0.8, 0.8, 0.8, 1),
		"inactivecaptiontext": (0.2, 0.2, 0.2, 1),
		"infobackground": (0.8, 0.8, 0.8, 1),
		"infotext": (0, 0, 0, 1),
		"menu": (0.8, 0.8, 0.8, 1),
		"menutext": (0.2, 0.2, 0.2, 1),
		"scrollbar": (0.8, 0.8, 0.8, 1),
		"threeddarkshadow": (0.2, 0.2, 0.2, 1),
		"threedface": (0.8, 0.8, 0.8, 1),
		"threedhighlight": (1, 1, 1, 1),
		"threedlightshadow": (0.2, 0.2, 0.2, 1),
		"threedshadow": (0.2, 0.2, 0.2, 1),
		"window": (0.8, 0.8, 0.8, 1),
		"windowframe": (0.8, 0.8, 0.8, 1),
		"windowtext": (0, 0, 0, 1),
		"none": (0, 0, 0, 0),
		"transparent": (0, 0, 0, 0),
	}
	if colour is None or colour not in colours:
		return (0, 0, 0, 0)
	return (
		int(colours[colour][0] * 255),
		int(colours[colour][1] * 255),
		int(colours[colour][2] * 255),
		int(colours[colour][3] * 255),
	)
