from src.modules.data_loader import load_data


def test_load_data():
    EPSILON: float = pow(10, -4)
    data: tuple[tuple[str, float], ...] = tuple(load_data())
    d0 = data[0]
    assert d0[0] == "srgb"
    assert abs(d0[1] - 0.085) < EPSILON
    d1 = data[1]
    assert d1[0] == "p3"
    assert abs(d1[1] - 0.113) < EPSILON
    d2 = data[2]
    assert d2[0] == "rec2020"
    assert abs(d2[1] - 0.120) < EPSILON
