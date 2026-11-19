from grades import checkgrades


def test_checkgrades():
    assert checkgrades(500) is not None
