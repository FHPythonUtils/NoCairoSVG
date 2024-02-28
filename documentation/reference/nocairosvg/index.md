# Nocairosvg

[Nocairosvg Index](../README.md#nocairosvg-index) / Nocairosvg

> Auto-generated documentation for [nocairosvg](../../../nocairosvg/__init__.py) module.

- [Nocairosvg](#nocairosvg)
  - [colour2tuple](#colour2tuple)
  - [convert](#convert)
  - [resolve_file_url](#resolve_file_url)
  - [svg2bitmap](#svg2bitmap)
  - [svg2eps](#svg2eps)
  - [svg2pdf](#svg2pdf)
  - [svg2png](#svg2png)
  - [svg2ps](#svg2ps)
  - [svg2svg](#svg2svg)
  - [write](#write)

## colour2tuple

[Show source in __init__.py:447](../../../nocairosvg/__init__.py#L447)

Convert a colour string to tuple

#### Arguments

- `colour` *Optional[str]* - the colour

#### Returns

Tuple[int, int, int, int]: the converted colour

#### Signature

```python
def colour2tuple(colour: str | None) -> tuple[int, int, int, int]: ...
```



## convert

[Show source in __init__.py:411](../../../nocairosvg/__init__.py#L411)

Launch playwright and use the html canvas to convert

#### Arguments

- `url` *str* - location of the image to convert
background_colour (Tuple[int, int, int, int], optional): Set the background colour.
Defaults to (0, 0, 0, 0).
size (Tuple[Optional[int], Optional[int]], optional): Size to crop the image to.
Defaults to (None, None).

#### Returns

- `Image.Image` - PIL Image

#### Signature

```python
def convert(
    url: str,
    background_colour: tuple[int, int, int, int] = (0, 0, 0, 0),
    size: tuple[int | None, int | None] = (None, None),
) -> Image.Image: ...
```



## resolve_file_url

[Show source in __init__.py:364](../../../nocairosvg/__init__.py#L364)

Get a file url from a bytestring, file object, or url...

#### Arguments

- `bytestring` *Optional[bytes], optional* - svg bytes. Defaults to None.
- `file_obj` *Optional[FileIO], optional* - file object. Defaults to None.
- `url` *Optional[str], optional* - path. Defaults to None.

#### Returns

- `str` - path

#### Signature

```python
def resolve_file_url(
    bytestring: bytes | None = None,
    file_obj: FileIO | None = None,
    url: str | None = None,
) -> str: ...
```



## svg2bitmap

[Show source in __init__.py:298](../../../nocairosvg/__init__.py#L298)

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

#### Signature

```python
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
) -> bytes | None: ...
```



## svg2eps

[Show source in __init__.py:235](../../../nocairosvg/__init__.py#L235)

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

#### Signature

```python
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
) -> bytes | None: ...
```



## svg2pdf

[Show source in __init__.py:126](../../../nocairosvg/__init__.py#L126)

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

#### Signature

```python
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
) -> bytes | None: ...
```



## svg2png

[Show source in __init__.py:64](../../../nocairosvg/__init__.py#L64)

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

#### Signature

```python
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
) -> bytes | None: ...
```



## svg2ps

[Show source in __init__.py:189](../../../nocairosvg/__init__.py#L189)

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

#### Signature

```python
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
) -> bytes | None: ...
```



## svg2svg

[Show source in __init__.py:18](../../../nocairosvg/__init__.py#L18)

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

#### Signature

```python
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
) -> bytes | None: ...
```



## write

[Show source in __init__.py:392](../../../nocairosvg/__init__.py#L392)

Write the pil image to the filesystem

#### Arguments

- `image` *Image.Image* - pillow image
file (Union[str, FileIO, None]): the file
- `ext` *str* - the image extension
- `dpi` *int* - the dpi

#### Returns

- `Optional[bytes]` - the image data in bytes if no file specified

#### Signature

```python
def write(
    image: Image.Image, file: str | FileIO | None, ext: str, dpi: int
) -> bytes | None: ...
```