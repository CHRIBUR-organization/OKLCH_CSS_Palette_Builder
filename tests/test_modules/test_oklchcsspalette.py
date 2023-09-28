import pytest

from src.modules.oklchcsspalette import OklchCssPaletteBuilder


@pytest.mark.parametrize(
    "min_lightness, max_lightness, step_lightness, min_hue, max_hue, step_hue",
    (
        (-1, 35, 5, 27, 54, 5),
        (1, 1000, 2, 2, 98, 2),
        (35, 2, 1, 0, 200, 4),
        (27, 54, 5, -1, 35, 5),
        (2, 98, 2, 1, 1000, 2),
        (0, 70, 4, 35, 2, 1),
        (0, 100, 1, 0, 359, 1)
    )
)
def test_oklch_css_palette_builder(
    min_lightness: int,
    max_lightness: int,
    step_lightness: int,
    min_hue: int,
    max_hue: int,
    step_hue: int,
):
    with pytest.raises(ValueError):
        OklchCssPaletteBuilder(
            min_lightness, max_lightness, step_lightness, min_hue, max_hue, step_hue
        )
