# nocairosvg

> Auto-generated documentation for [nocairosvg](../../nocairosvg/__init__.py) module.

- [Nocairosvg_](../README.md#nocairosvg_-index) / [Modules](../README.md#nocairosvg_-modules) / nocairosvg
    - [colour2Tuple](#colour2tuple)
    - [convertSVG](#convertsvg)
    - [findAndReplace](#findandreplace)
    - [getSize](#getsize)
    - [resolveFileURL](#resolvefileurl)
    - [svg2bitmap](#svg2bitmap)
    - [svg2eps](#svg2eps)
    - [svg2pdf](#svg2pdf)
    - [svg2png](#svg2png)
    - [svg2ps](#svg2ps)
    - [svg2svg](#svg2svg)
    - [takeScreenshot](#takescreenshot)
    - [write](#write)

## colour2Tuple

[[find in source code]](../../nocairosvg/__init__.py#L412)

```python
def colour2Tuple(colour: Optional[str]) -> Tuple[(int, int, int, int)]:
```

Convert a colour string to tuple

#### Arguments

- `colour` *Optional[str]* - the colour

#### Returns

Tuple[int, int, int, int]: the converted colour

## convertSVG

[[find in source code]](../../nocairosvg/__init__.py#L340)

```python
def convertSVG(
    url: str,
    transparentColour: Optional[Tuple[(int, int, int, int)]] = None,
    backgroundColour: Tuple[(int, int, int, int)] = (0, 0, 0, 0),
    size: Tuple[(Optional[int], Optional[int])] = (None, None),
) -> Image.Image:
```

Convert an SVG to a pillow Image

#### Arguments

- `url` *str* - the path to the file
   transparentColour (Optional[Tuple[int, int, int, int]], optional): The
   colour to replace with transparent/ background. Defaults to None.
   backgroundColour (Optional[Tuple[int, int, int, int]], optional): The
   background colour. Defaults to (0,0,0,0).
   size (Tuple[Optional[int], Optional[int]], optional): Sizes passed by
   user. Defaults to (None, None).

#### Returns

- `Image.Image` - [description]

## findAndReplace

[[find in source code]](../../nocairosvg/__init__.py#L377)

```python
def findAndReplace(
    image: Image.Image,
    find: Tuple[(int, int, int, int)],
    replace: Tuple[(int, int, int, int)],
    threshold: int = 3,
):
```

Find and replace colour in PIL Image

#### Arguments

- `image` *PIL.Image.Image* - The Image
- `find` *(r,g,b,a)* - A tuple containing values for rgba from 0-255 inclusive
- `replace` *(r,g,b,a)* - A tuple containing values for rgba from 0-255 inclusive
- `threshold` *int, optional* - Find and replace without an exact match.
Default is 3

#### Returns

- `PIL.Image.Image` - The result

## getSize

[[find in source code]](../../nocairosvg/__init__.py#L306)

```python
async def getSize(url: str) -> dict[(str, float)]:
```

Get the image size

#### Arguments

- `url` *str* - the path to the svg

#### Returns

- `dict[str,` *float]* - the size

## resolveFileURL

[[find in source code]](../../nocairosvg/__init__.py#L264)

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

[[find in source code]](../../nocairosvg/__init__.py#L208)

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

[[find in source code]](../../nocairosvg/__init__.py#L168)

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

## svg2pdf

[[find in source code]](../../nocairosvg/__init__.py#L91)

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

## svg2png

[[find in source code]](../../nocairosvg/__init__.py#L52)

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

## svg2ps

[[find in source code]](../../nocairosvg/__init__.py#L131)

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

## svg2svg

[[find in source code]](../../nocairosvg/__init__.py#L15)

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

## takeScreenshot

[[find in source code]](../../nocairosvg/__init__.py#L329)

```python
async def takeScreenshot(
    url: str,
    resolution: Tuple[(int, int)] = (100, 100),
):
```

Go to a URL, with a browser with a set resolution

## write

[[find in source code]](../../nocairosvg/__init__.py#L286)

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
