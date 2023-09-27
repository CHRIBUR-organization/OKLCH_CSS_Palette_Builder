"""
make_oklch_css_palette
license: MIT License
Copyright © 2023 CHRIBUR_. All rights reserved.
"""

__author__ = "クリバ (CHRIBUR_)"

from typing import Iterator


class OklchCssPaletteBuilder:
    """
    The builder class which builds an OKLCH CSS color palette.
    OKLCH is a uniform color space designed by Björn Ottosson in 2020 [1].
    You can use it as CSS Color Module Level 4 with most modern browsers [2].

    Attributes
    -------
    __min_lightness : int
        The min value of the lightness in the palette you want to use.
    __max_lightness : int
        The max value of the lightness in the palette you want to use.
        Depending on the pair of __min_lightness and __step_lightness values,
        the max value of lightness used may be smaller than __max_lightness.
    __step_lightness : int
        The step value of the lightness in the palette you want to use.
    __min_hue : int
        The min value of the hue in the palette you want to use.
    __max_hue : int
        The max value of the hue in the palette you want to use.
        Depending on the pair of __min_hue and __step_hue values,
        the max value of hue used may be smaller than __max_hue.
    __step_hue : int
        The step value of the hue in the palette you want to use.
    __mid_lightness : float
        The average of the __min_lightness and __max_lightness values.
        It is used in __calc_chroma().

    Notes
    ------
    [1] B. Ottosson. "A perceptual color space for image processing."
    Björn Ottosson. https://bottosson.github.io/posts/oklab/
    (accessed Sep. 25, 2023).

    [2] "oklch." Can I use... Support tables for HTML5, CSS3, etc.
    https://caniuse.com/?search=oklch (accessed Sep. 25, 2023).
    """

    __gamut_max_chroma: tuple[tuple[str, float], ...] = (
        ("srgb", 0.085),
        ("p3", 0.113),
        ("rec2020", 0.120),
    )

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
        __max_lightness : int
            It must be equal or less than 100.
        __step_lightness : int
            It must be positive.
        __min_hue : int
            It must not be negative.
        __max_hue : int
            It must be equal or greater than 359.
        __step_hue : int
            It must be positive.

        Raises
        ------
        ValueError
            If not 0 <= self.__min_lightness < self.__max_lightness <= 100,
            "Illegal lightness range" error will be raised.
        ValueError
            If not 0 <= self.__min_hue < self.__max_hue <= 359,
            "Illegal hue range" error will be raised.
        """
        self.__min_lightness: int = min_lightness
        self.__max_lightness: int = max_lightness
        if not 0 <= self.__min_lightness < self.__max_lightness <= 100:
            raise ValueError("Illegal lightness range.")
        self.__step_lightness: int = step_lightness
        self.__min_hue: int = min_hue
        self.__max_hue: int = max_hue
        if not 0 <= self.__min_hue < self.__max_hue <= 359:
            raise ValueError("Illegal hue range.")
        self.__step_hue: int = step_hue
        self.__mid_lightness: float = (
            self.__min_lightness + self.__max_lightness
        ) / 2.0

    def __calc_chroma(self, lightness: int, max_chroma: float) -> float:
        """
        The function which calculates the chroma value for a given lightness.
        You cannot call it.

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
            -abs(lightness - self.__mid_lightness) / self.__mid_lightness + 1.0
        )

    def __css_data_iterator(self) -> Iterator[str]:
        """
        The iterator which yields the lines of the CSS file you will get.
        You cannot call it.

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
        num_gamuts: int = len(OklchCssPaletteBuilder.__gamut_max_chroma)
        for i, gm in enumerate(OklchCssPaletteBuilder.__gamut_max_chroma):
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
            It should be ended with ".css".
        """
        with open(css_filepath, "w", encoding="utf8") as f:
            f.writelines(map(lambda x: f"{x}\n", self.__css_data_iterator()))


def main() -> None:
    min_lightness = int(input("minimum lightness = "))
    max_lightness = int(input("maximum lightness = "))
    step_lightness = int(input("step of lightness = "))
    min_hue = int(input("minimum hue = "))
    max_hue = int(input("maximum hue = "))
    step_hue = int(input("step of hue = "))
    ocpb = OklchCssPaletteBuilder(
        min_lightness, max_lightness, step_lightness, min_hue, max_hue, step_hue
    )
    css_filepath = input("CSS file path: ")
    ocpb.make_css(css_filepath)


if __name__ == "__main__":
    main()
