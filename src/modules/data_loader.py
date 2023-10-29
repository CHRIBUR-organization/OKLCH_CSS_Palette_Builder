from pathlib import Path
from typing import Iterator


def load_data() -> Iterator[str]:
    """
    It loads the data of gamuts and yields their unformatted information.

    Yields
    ------
    str
        The unformatted information of a gamut.
    """
    data_path: Path = (
        Path(__file__).parent / ".." / "data" / "gamut_data.txt"
    ).resolve()
    with data_path.open(encoding="utf8") as f:
        return (line.rstrip() for line in f.readlines())


def format_data(data_lines: Iterator[str]) -> Iterator[tuple[str, float]]:
    """
    It formats the gamut data information.

    Parameters
    ----------
    data_lines : Iterator[str]
        The unformatted information of a gamut.

    Yields
    ------
    tuple[str, float]
        The formatted information of a gamut.
    """
    for data in data_lines:
        d1, d2 = data.split(" ")
        yield d1, float(d2)
