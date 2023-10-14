from pathlib import Path
from typing import Iterator


def load_data() -> Iterator[tuple[str, float]]:
    """
    It loads the data of gamuts and yields their information.

    Yields
    ------
    tuple[str, float]
        The information of a gamut.
    """
    data_path: Path = (
        Path(__file__).parent / ".." / "data" / "gamut_data.txt"
    ).resolve()
    with data_path.open(encoding="utf8") as f:
        buf: Iterator[list[str]] = (data.split(" ") for data in f.readlines())
    return ((i[0], float(i[1])) for i in buf)
