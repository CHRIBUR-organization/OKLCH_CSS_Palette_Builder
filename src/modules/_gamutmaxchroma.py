from typing import NamedTuple


class GamutMaxChroma(NamedTuple):
    """
    The data class of the given gamut and its maximum value of chroma.

    Parameters
    ----------
    name : str
        The name of the given gamut.
    max_chroma : float
        The maximum value of chroma of the given gamut.
    """

    name: str
    max_chroma: float
