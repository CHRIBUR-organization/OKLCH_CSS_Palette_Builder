# OKLCH_CSS_Palette_Builder

![PyPI - Version](https://img.shields.io/pypi/v/oklchcsspalette)
[![CI](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/blank.yml/badge.svg)](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/blank.yml)
[![Python package](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/python-package.yml/badge.svg)](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/python-package.yml)
[![CodeQL](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/codeql.yml/badge.svg)](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/codeql.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub repo size](https://img.shields.io/github/repo-size/CHRIBUR0309/OKLCH_CSS_Palette_Builder)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1bae4f492011473689f1c6c3981320ea)](https://app.codacy.com/gh/CHRIBUR0309/OKLCH_CSS_Palette_Builder/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

You can make OKLCH CSS palettes using this!

## What is this?

This is a Python library which makes OKLCH CSS palettes.
OKLCH is a perceptually uniform color space designed by Björn Ottosson in 2020 (you can read [his blog](https://bottosson.github.io/posts/oklab/)).
You can use it as CSS Color Module Level 4 with the most of modern browsers (check [Can I Use...](https://caniuse.com/?search=oklch)).

Although we can use [OKLCH Color Picker & Converter](https://oklch.com), I think it is not easy to use because the surface of OKLCH is not flat.
So I wrote this library for CSS developers.

## Installation

```Shell
pip install oklchcsspalette
```

## How to use?

With Python >= 3.9, you can use this library as below.

```Python
from sys import argv

from oklchcsspalette import OklchCssPaletteBuilder

def main():
    attributes = tuple(map(int, argv[1:7]))
    ocpb = OklchCssPaletteBuilder(*attributes)
    ocpb.make_css(argv[7])

if __name__ == "__main__":
    main()

```

The attributes are int values needed to calcurate chromas on OKLCH space.

The argv[7] is a CSS file path. It must ends with ".css" (upper cases are ok).

## Contrast ratio with srgb

For the web accessibility, the necessary minimum of the diffs of lightnesses are below.

- At least 3:1 (Level AA of large scale of text) -> 35
- At least 4.5:1 (Level AA of text or Level AAA of large scale of text) -> 45
- At least 7:1 (Level AAA of text) -> 55

I calculated these values on a gray scale (chroma = 0). I have not checked on other colors (chroma > 0), but I think I will get similar results.

With p3 and rec2020, a contrast ratio is not defined, but I think we can use these values.

## License

[MIT License](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/blob/main/LICENSE)

## Attention

- This library does not yield Tailwind CSS color names.
- This library outputs duplicated colors; black and white.
