from calculator import multi

def test_positive():
    assert multi(2, 2) == 4, "2 * 2 != 4"
    assert multi(3, 3) == 9, "3 * 3 != 9"

def test_negative():
    assert multi(-2, -2) == 4, "-2 * -2 != 4"