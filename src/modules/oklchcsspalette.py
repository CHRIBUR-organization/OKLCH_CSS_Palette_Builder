"""
oklchcsspalette
license: MIT License
Copyright © 2023 CHRIBUR_. All rights reserved.
"""

__author__ = "クリバ (CHRIBUR_)"
__version__ = "1.0.5"

from typing import Iterator, NamedTuple
from pathlib import Path


class GamutMaxChroma(NamedTuple):
    """
    The data class of the given gamut and its max value of chroma.

    Parameters
    ----------
    name : str
        The name of the given gamut.
    max_chroma : float
        The max value of chroma of the given gamut.
    """
    name: str
    max_chroma: float


class OklchCssPaletteBuilder:
    """
    The builder class which builds an OKLCH CSS color palette.
    OKLCH is a uniform color space designed by Björn Ottosson in 2020 [1].
    You can use it as CSS Color Module Level 4 with most modern browsers [2].

    Attributes
    -------
    __min_lightness : int
        The min value of lightness in the palette you want to use.
    __max_lightness : int
        The max value of lightness in the palette you want to use.
        Depending on the pair of __min_lightness and __step_lightness values,
        the max value of lightness used may be smaller than __max_lightness.
    __step_lightness : int
        The step value of lightness in the palette you want to use.
    __min_hue : int
        The min value of hue in the palette you want to use.
    __max_hue : int
        The max value of hue in the palette you want to use.
        Depending on the pair of __min_hue and __step_hue values,
        the max value of hue used may be smaller than __max_hue.
    __step_hue : int
        The step value of hue in the palette you want to use.

    Notes
    ------
    [1] B. Ottosson. "A perceptual color space for image processing."
    Björn Ottosson. https://bottosson.github.io/posts/oklab/
    (accessed Sep. 25, 2023).

    [2] "oklch." Can I use... Support tables for HTML5, CSS3, etc.
    https://caniuse.com/?search=oklch (accessed Sep. 25, 2023).
    """

    __GAMUT_MAX_CHROMA: tuple[GamutMaxChroma, ...] = (
        GamutMaxChroma("srgb", 0.085),
        GamutMaxChroma("p3", 0.113),
        GamutMaxChroma("rec2020", 0.120),
    )
    __MINIMUM_LIGHTNESS: int = 0
    __MAXIMUM_LIGHTNESS: int = 100
    __MINIMUM_HUE: int = 0
    __MAXIMUM_HUE: int = 359
    __MEDIAN_LIGHTNESS: int = (__MINIMUM_LIGHTNESS + __MAXIMUM_LIGHTNESS) >> 1

    def __init__(
        self,
        min_lightness: int,
        max_lightness: int,
        step_lightness: int,
        min_hue: int,
        max_hue: int,
        step_hue: int,
    ) -> None:
        """
        The constructor of the OklchCssPaletteBuilder class.
        It gets the ranges of lightness and hue you want to use.

        Parameters
        ----------
        min_lightness : int
            It must not be negative.
        max_lightness : int
            It must be equal or less than 100.
        step_lightness : int
            It must be positive.
        min_hue : int
            It must not be negative.
        max_hue : int
            It must be equal or greater than 359.
        step_hue : int
            It must be positive.

        Raises
        ------
        ValueError
            If not 0 <= self.__min_lightness < self.__max_lightness <= 100,
            "Invalid lightness range" error will be raised.
        ValueError
            If not 0 <= self.__min_hue < self.__max_hue <= 359,
            "Invalid hue range" error will be raised.
        """
        self.__min_lightness: int = min_lightness
        self.__max_lightness: int = max_lightness
        if (
            not OklchCssPaletteBuilder.__MINIMUM_LIGHTNESS
            <= self.__min_lightness
            < self.__max_lightness
            <= OklchCssPaletteBuilder.__MAXIMUM_LIGHTNESS
        ):
            raise ValueError(
                f"Invalid lightness range. Must be {OklchCssPaletteBuilder.__MINIMUM_LIGHTNESS} <= min_lightness < max_lightness <= {OklchCssPaletteBuilder.__MAXIMUM_LIGHTNESS}."
            )
        self.__step_lightness: int = step_lightness
        self.__min_hue: int = min_hue
        self.__max_hue: int = max_hue
        if (
            not OklchCssPaletteBuilder.__MINIMUM_HUE
            <= self.__min_hue
            < self.__max_hue
            <= OklchCssPaletteBuilder.__MAXIMUM_HUE
        ):
            raise ValueError(
                f"Invalid hue range. Must be {OklchCssPaletteBuilder.__MINIMUM_HUE} <= min_hue < max_hue <= {OklchCssPaletteBuilder.__MAXIMUM_HUE}."
            )
        self.__step_hue: int = step_hue

    def __calc_chroma(self, lightness: int, max_chroma: float) -> float:
        """
        The function which calculates the chroma value for the given lightness.
        You cannot call it directly.

        Parameters
        ----------
        lightness : int
            A variable of the lightness.
        max_chroma : float
            A float value come from a gamut.

        Returns
        -------
        float
            The chroma value for the given lightness.
        """
        return max_chroma * (
            -abs(lightness - OklchCssPaletteBuilder.__MEDIAN_LIGHTNESS)
            / OklchCssPaletteBuilder.__MEDIAN_LIGHTNESS
            + 1.0
        )

    def __css_data_iterator(self) -> Iterator[str]:
        """
        The iterator which yields the lines of the CSS file you will get.
        You cannot call it directly.

        Yields
        ------
        str
            The lines of the CSS file you will get.
        """
        lightnesses: tuple[int, ...] = tuple(
            range(self.__min_lightness, self.__max_lightness + 1, self.__step_lightness)
        )
        hues: tuple[str, ...] = ("gray",) + tuple(
            map(str, range(self.__min_hue, self.__max_hue + 1, self.__step_hue))
        )
        num_hues: int = len(hues)
        num_lightnesses: int = len(lightnesses)
        num_gamuts: int = len(OklchCssPaletteBuilder.__GAMUT_MAX_CHROMA)
        for i, gm in enumerate(OklchCssPaletteBuilder.__GAMUT_MAX_CHROMA):
            gamut, max_chroma = gm
            if gamut == "srgb":
                header = ":root {"
                indent = "  "
                footer = "}"
            else:
                header = f"@media (color-gamut: {gamut}) {{\n  :root {{"
                indent = "    "
                footer = "  }\n}"
            yield header
            chromas: tuple[str, ...] = tuple(
                map(
                    lambda x: f"{self.__calc_chroma(x, max_chroma):.5f}"[1:],
                    lightnesses,
                )
            )
            for j, hue in enumerate(hues):
                if hue == "gray":
                    for light in lightnesses:
                        yield f"{indent}--color-{hue}-lightness-{light}: oklch({light}% 0 0),"
                else:
                    for k, lc in enumerate(zip(lightnesses, chromas)):
                        light, chroma = lc
                        buf = f"{indent}--color-hue-{hue}-lightness-{light}: oklch({light}% {chroma} {hue})"
                        if j == num_hues - 1 and k == num_lightnesses - 1:
                            yield buf
                        else:
                            yield f"{buf},"
            yield footer
            if i <= num_gamuts - 2:
                yield ""

    def make_css(self, css_filepath: str) -> None:
        """
        The function which writes the CSS file to the given path.

        Parameters
        ----------
        css_filepath : str
            The path to the CSS file you will get.
            It must ends with ".css".

        Raises
        ----------
        ValueError
            If the extension of the given path is not ".css",
            "Invalid file extension" error will be raised.
        """
        path: Path = Path(css_filepath)
        if path.suffix.lower() != ".css":
            raise ValueError("Invalid file extension. Must be '.css'.")
        parent: Path = path.parent
        if not parent.exists():
            parent.mkdir(parents=True)
        with path.open("w", encoding="utf8") as f:
            f.writelines(map(lambda line: f"{line}\n", self.__css_data_iterator()))
