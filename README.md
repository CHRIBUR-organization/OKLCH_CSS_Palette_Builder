# OKLCH_CSS_Palette_Builder

[![CI](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/blank.yml/badge.svg)](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/blank.yml)
[![Python package](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/python-package.yml/badge.svg)](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/python-package.yml)
[![CodeQL](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/codeql.yml/badge.svg)](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/actions/workflows/codeql.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

You can make OKLCH CSS palettes using this!

## What is this?

This is a Python library which makes OKLCH CSS palettes.
OKLCH is a perceptually uniform color space designed by Björn Ottosson in 2020 (you can read [his blog](https://bottosson.github.io/posts/oklab/)).
You can use it as CSS Color Module Level 4 with most modern browsers (check [Can I Use...](https://caniuse.com/?search=oklch)).

Although we can use [OKLCH Color Picker & Converter](https://oklch.com), I think it is not easy to use because the surface of OKLCH is not flat.
So I wrote this library for CSS developers.

## Installation

```Shell
pip install make_oklch_css_palette
```

## License

[MIT License](https://github.com/CHRIBUR0309/OKLCH_CSS_Palette_Builder/blob/main/LICENSE)

## Attention

- This library does not yield Tailwind CSS color names.
- This library outputs duplicated colors; black and white.
