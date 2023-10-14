from src.modules.gamutmaxchroma import GamutMaxChroma


def test_gamutmaxchroma():
    testdata_str: str = "foo"
    testdata_float: float = 0.1
    EPSILON: float = pow(10, -4)
    gmc = GamutMaxChroma(testdata_str, testdata_float)
    assert gmc.name == testdata_str
    assert abs(gmc.max_chroma - testdata_float) < EPSILON
