from wordhunt import is_adjacent


def test_is_adjacent() -> None:
    assert is_adjacent((0, 0), (1, 1))
    assert is_adjacent((0, 0), (1, 0))
    assert is_adjacent((0, 0), (0, 1))
    assert not is_adjacent((0, 0), (2, 1))
