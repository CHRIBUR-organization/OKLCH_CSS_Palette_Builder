from src.modules.data_loader import format_data, load_data


def test_load_data():
    data_lines: tuple[str] = tuple(load_data())
    d0, d1, d2 = data_lines
    assert d0 == "srgb 0.085"
    assert d1 == "p3 0.113"
    assert d2 == "rec2020 0.120"


def test_format_data():
    data_lines: list[str] = ["foo 0.5", "bar 1.0", "baz 1.5"]
    EPSILON: float = 1e-4
    formatted_data: tuple[tuple[str, float], ...] = tuple(format_data(data_lines))
    d0, d1, d2 = formatted_data
    d00, d01 = d0
    assert d00 == "foo"
    assert abs(d01 - 0.5) < EPSILON
    d10, d11 = d1
    assert d10 == "bar"
    assert abs(d11 - 1.0) < EPSILON
    d20, d21 = d2
    assert d20 == "baz"
    assert abs(d21 - 1.5) < EPSILON
