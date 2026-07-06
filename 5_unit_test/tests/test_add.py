from calculator import add


def test_positive():
    assert add(2, 2) == 4, "2 + 2 != 4"
    assert add(3, 3) == 6, "3 + 3 != 6"

def test_negative():
    assert add(-1, -1), "-1 -1 != -2"
