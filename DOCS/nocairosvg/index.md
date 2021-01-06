# nocairosvg

> Auto-generated documentation for [nocairosvg](../../nocairosvg/__init__.py) module.

- [Nocairosvg](../README.md#nocairosvg-index) / [Modules](../README.md#nocairosvg-modules) / nocairosvg
    - [colour2Tuple](#colour2tuple)
    - [convert](#convert)
    - [resolveFileURL](#resolvefileurl)
    - [svg2bitmap](#svg2bitmap)
    - [svg2eps](#svg2eps)
    - [svg2pdf](#svg2pdf)
    - [svg2png](#svg2png)
    - [svg2ps](#svg2ps)
    - [svg2svg](#svg2svg)
    - [write](#write)

## colour2Tuple

[[find in source code]](../../nocairosvg/__init__.py#L344)

```python
def colour2Tuple(colour: Optional[str]) -> Tuple[(int, int, int, int)]:
```

Convert a colour string to tuple

#### Arguments

- `colour` *Optional[str]* - the colour

#### Returns

Tuple[int, int, int, int]: the converted colour

## convert

[[find in source code]](../../nocairosvg/__init__.py#L312)

```python
async def convert(
    url: str,
    backgroundColour: Tuple[(int, int, int, int)] = (0, 0, 0, 0),
    size: Tuple[(Optional[int], Optional[int])] = (None, None),
) -> Image.Image:
```

Launch pyppeteer and use the html canvas to convert

#### Arguments

- `url` *str* - location of the image to convert
backgroundColour (Tuple[int, int, int, int], optional): Set the background colour.
Defaults to (0, 0, 0, 0).
size (Tuple[Optional[int], Optional[int]], optional): Size to crop the image to.
Defaults to (None, None).

#### Returns

- `Image.Image` - PIL Image

## resolveFileURL

[[find in source code]](../../nocairosvg/__init__.py#L266)

```python
def resolveFileURL(
    bytestring: Optional[bytes] = None,
    file_obj: Optional[FileIO] = None,
    url: Optional[str] = None,
) -> str:
```

Get a file url from a bytestring, file object, or url...

#### Arguments

- `bytestring` *Optional[bytes], optional* - svg bytes. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - file object. Defaults to None.
- `url` *Optional[str], optional* - path. Defaults to None.

#### Returns

- `str` - path

## svg2bitmap

[[find in source code]](../../nocairosvg/__init__.py#L209)

```python
def svg2bitmap(
    bytestring: Optional[bytes] = None,
    file_obj: Optional[FileIO] = None,
    url: Optional[str] = None,
    dpi: int = 96,
    parent_width: Optional[int] = None,
    parent_height: Optional[int] = None,
    scale: float = 1,
    background_color: Optional[str] = None,
    negate_colors: bool = False,
    invert_images: bool = False,
    write_to: Union[(str, FileIO, None)] = None,
    output_width: Optional[int] = None,
    output_height: Optional[int] = None,
    ext: str = 'png',
    transparent: bool = True,
) -> Optional[bytes]:
```

Convert an SVG to an SVG

#### Arguments

- `bytestring` *Optional[bytes], optional* - bytes containing svg data. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - opened file object. Defaults to None.
- `url` *Optional[str], optional* - path to file. Defaults to None.
- `dpi` *int, optional* - dpi. Defaults to 96.
- `parent_width` *Optional[int], optional* - width of the parent element
(e.g. div). Defaults to None.
- `parent_height` *Optional[int], optional* - height of the parent element
(e.g. div). Defaults to None.
- `scale` *float, optional* - scale the image by . Defaults to 1.
- `background_color` *Optional[str], optional* - Set a bg colour if not
transparent. Defaults to None.
- `negate_colors` *bool, optional* - invert the image colours. Defaults to False.
- `invert_images` *bool, optional* - invert the image colours. Defaults to False.
write_to (Union[str, FileIO, None], optional): file path/ object to
write to (Omit to return bytes). Defaults to None.
- `output_width` *Optional[int], optional* - width of output image. Defaults to None.
- `output_height` *Optional[int], optional* - height of output image.
Defaults to None.
- `ext` *str* - image type. Defaults to 'png'
- `transparent` *bool* - Should the image be transparent. Defaults to True

#### Returns

- `Optional[bytes]` - Bytes of image if write_to is None. else writes image
to file

## svg2eps

[[find in source code]](../../nocairosvg/__init__.py#L169)

```python
def svg2eps(
    bytestring: Optional[bytes] = None,
    file_obj: Optional[FileIO] = None,
    url: Optional[str] = None,
    dpi: int = 96,
    parent_width: Optional[int] = None,
    parent_height: Optional[int] = None,
    scale: float = 1,
    unsafe: bool = False,
    background_color: Optional[str] = None,
    negate_colors: bool = False,
    invert_images: bool = False,
    write_to: Union[(str, FileIO, None)] = None,
    output_width: Optional[int] = None,
    output_height: Optional[int] = None,
) -> Optional[bytes]:
```

Convert an SVG to EPS

#### Arguments

- `bytestring` *Optional[bytes], optional* - bytes containing svg data. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - opened file object. Defaults to None.
- `url` *Optional[str], optional* - path to file. Defaults to None.
- `dpi` *int, optional* - dpi. Defaults to 96.
- `parent_width` *Optional[int], optional* - width of the parent element
(e.g. div). Defaults to None.
- `parent_height` *Optional[int], optional* - height of the parent element
(e.g. div). Defaults to None.
- `scale` *float, optional* - scale the image by . Defaults to 1.
- `unsafe` *bool, optional* - NA here . Defaults to False.
- `background_color` *Optional[str], optional* - Set a bg colour if not
transparent. Defaults to None.
- `negate_colors` *bool, optional* - invert the image colours. Defaults to False.
- `invert_images` *bool, optional* - invert the image colours. Defaults to False.
write_to (Union[str, FileIO, None], optional): file path/ object to
write to (Omit to return bytes). Defaults to None.
- `output_width` *Optional[int], optional* - width of output image. Defaults to None.
- `output_height` *Optional[int], optional* - height of output image.
Defaults to None.

#### Returns

- `Optional[bytes]` - Bytes of image if write_to is None. else writes image
to file

## svg2pdf

[[find in source code]](../../nocairosvg/__init__.py#L92)

```python
def svg2pdf(
    bytestring: Optional[bytes] = None,
    file_obj: Optional[FileIO] = None,
    url: Optional[str] = None,
    dpi: int = 96,
    parent_width: Optional[int] = None,
    parent_height: Optional[int] = None,
    scale: float = 1,
    unsafe: bool = False,
    background_color: Optional[str] = None,
    negate_colors: bool = False,
    invert_images: bool = False,
    write_to: Union[(str, FileIO, None)] = None,
    output_width: Optional[int] = None,
    output_height: Optional[int] = None,
) -> Optional[bytes]:
```

Convert an SVG to a PDF

#### Arguments

- `bytestring` *Optional[bytes], optional* - bytes containing svg data. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - opened file object. Defaults to None.
- `url` *Optional[str], optional* - path to file. Defaults to None.
- `dpi` *int, optional* - dpi. Defaults to 96.
- `parent_width` *Optional[int], optional* - width of the parent element
(e.g. div). Defaults to None.
- `parent_height` *Optional[int], optional* - height of the parent element
(e.g. div). Defaults to None.
- `scale` *float, optional* - scale the image by . Defaults to 1.
- `unsafe` *bool, optional* - NA here . Defaults to False.
- `background_color` *Optional[str], optional* - Set a bg colour if not
transparent. Defaults to None.
- `negate_colors` *bool, optional* - invert the image colours. Defaults to False.
- `invert_images` *bool, optional* - invert the image colours. Defaults to False.
write_to (Union[str, FileIO, None], optional): file path/ object to
write to (Omit to return bytes). Defaults to None.
- `output_width` *Optional[int], optional* - width of output image. Defaults to None.
- `output_height` *Optional[int], optional* - height of output image.
Defaults to None.

#### Returns

- `Optional[bytes]` - Bytes of image if write_to is None. else writes image
to file

## svg2png

[[find in source code]](../../nocairosvg/__init__.py#L53)

```python
def svg2png(
    bytestring: Optional[bytes] = None,
    file_obj: Optional[FileIO] = None,
    url: Optional[str] = None,
    dpi: int = 96,
    parent_width: Optional[int] = None,
    parent_height: Optional[int] = None,
    scale: float = 1,
    unsafe: bool = False,
    background_color: Optional[str] = None,
    negate_colors: bool = False,
    invert_images: bool = False,
    write_to: Union[(str, FileIO, None)] = None,
    output_width: Optional[int] = None,
    output_height: Optional[int] = None,
) -> Optional[bytes]:
```

Convert an SVG to a PNG

#### Arguments

- `bytestring` *Optional[bytes], optional* - bytes containing svg data. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - opened file object. Defaults to None.
- `url` *Optional[str], optional* - path to file. Defaults to None.
- `dpi` *int, optional* - dpi. Defaults to 96.
- `parent_width` *Optional[int], optional* - width of the parent element
(e.g. div). Defaults to None.
- `parent_height` *Optional[int], optional* - height of the parent element
(e.g. div). Defaults to None.
- `scale` *float, optional* - scale the image by . Defaults to 1.
- `unsafe` *bool, optional* - NA here . Defaults to False.
- `background_color` *Optional[str], optional* - Set a bg colour if not
transparent. Defaults to None.
- `negate_colors` *bool, optional* - invert the image colours. Defaults to False.
- `invert_images` *bool, optional* - invert the image colours. Defaults to False.
write_to (Union[str, FileIO, None], optional): file path/ object to
write to (Omit to return bytes). Defaults to None.
- `output_width` *Optional[int], optional* - width of output image. Defaults to None.
- `output_height` *Optional[int], optional* - height of output image.
Defaults to None.

#### Returns

- `Optional[bytes]` - Bytes of image if write_to is None. else writes image
to file

## svg2ps

[[find in source code]](../../nocairosvg/__init__.py#L132)

```python
def svg2ps(
    bytestring: Optional[bytes] = None,
    file_obj: Optional[FileIO] = None,
    url: Optional[str] = None,
    dpi: int = 96,
    parent_width: Optional[int] = None,
    parent_height: Optional[int] = None,
    scale: float = 1,
    unsafe: bool = False,
    background_color: Optional[str] = None,
    negate_colors: bool = False,
    invert_images: bool = False,
    write_to: Union[(str, FileIO, None)] = None,
    output_width: Optional[int] = None,
    output_height: Optional[int] = None,
) -> Optional[bytes]:
```

Convert an SVG to PS

#### Arguments

- `bytestring` *Optional[bytes], optional* - bytes containing svg data. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - opened file object. Defaults to None.
- `url` *Optional[str], optional* - path to file. Defaults to None.
- `dpi` *int, optional* - dpi. Defaults to 96.
- `parent_width` *Optional[int], optional* - width of the parent element
(e.g. div). Defaults to None.
- `parent_height` *Optional[int], optional* - height of the parent element
(e.g. div). Defaults to None.
- `scale` *float, optional* - scale the image by . Defaults to 1.
- `unsafe` *bool, optional* - NA here . Defaults to False.
- `background_color` *Optional[str], optional* - Set a bg colour if not
transparent. Defaults to None.
- `negate_colors` *bool, optional* - invert the image colours. Defaults to False.
- `invert_images` *bool, optional* - invert the image colours. Defaults to False.
write_to (Union[str, FileIO, None], optional): file path/ object to
write to (Omit to return bytes). Defaults to None.
- `output_width` *Optional[int], optional* - width of output image. Defaults to None.
- `output_height` *Optional[int], optional* - height of output image.
Defaults to None.

#### Returns

- `Optional[bytes]` - Bytes of image if write_to is None. else writes image
to file

## svg2svg

[[find in source code]](../../nocairosvg/__init__.py#L16)

```python
def svg2svg(
    bytestring: Optional[bytes] = None,
    file_obj: Optional[FileIO] = None,
    url: Optional[str] = None,
    dpi: int = 96,
    parent_width: Optional[int] = None,
    parent_height: Optional[int] = None,
    scale: float = 1,
    unsafe: bool = False,
    background_color: Optional[str] = None,
    negate_colors: bool = False,
    invert_images: bool = False,
    write_to: Union[(str, FileIO, None)] = None,
    output_width: Optional[int] = None,
    output_height: Optional[int] = None,
) -> Optional[bytes]:
```

Convert an SVG to an SVG

#### Arguments

- `bytestring` *Optional[bytes], optional* - bytes containing svg data. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - opened file object. Defaults to None.
- `url` *Optional[str], optional* - path to file. Defaults to None.
- `dpi` *int, optional* - dpi. Defaults to 96.
- `parent_width` *Optional[int], optional* - width of the parent element
(e.g. div). Defaults to None.
- `parent_height` *Optional[int], optional* - height of the parent element
(e.g. div). Defaults to None.
- `scale` *float, optional* - scale the image by . Defaults to 1.
- `unsafe` *bool, optional* - NA here . Defaults to False.
- `background_color` *Optional[str], optional* - Set a bg colour if not
transparent. Defaults to None.
- `negate_colors` *bool, optional* - invert the image colours. Defaults to False.
- `invert_images` *bool, optional* - invert the image colours. Defaults to False.
write_to (Union[str, FileIO, None], optional): file path/ object to
write to (Omit to return bytes). Defaults to None.
- `output_width` *Optional[int], optional* - width of output image. Defaults to None.
- `output_height` *Optional[int], optional* - height of output image.
Defaults to None.

#### Returns

- `Optional[bytes]` - Bytes of image if write_to is None. else writes image
to file

## write

[[find in source code]](../../nocairosvg/__init__.py#L292)

```python
def write(
    image: Image.Image,
    file: Union[(str, FileIO, None)],
    ext: str,
    dpi: int,
) -> Optional[bytes]:
```

Write the pil image to the filesystem

#### Arguments

- `image` *Image.Image* - pillow image
file (Union[str, FileIO, None]): the file
- `ext` *str* - the image extension
- `dpi` *int* - the dpi

#### Returns

- `Optional[bytes]` - the image data in bytes if no file specified
