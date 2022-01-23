from structures import Point


def test_point_eq():
    p1 = Point(1, 1)
    p2 = Point(1, 1)
    p3 = Point(2, 2)
    assert p1 == p2
    assert p1 != p3


def test_point_add():
    p1 = Point(1, 1)
    p2 = Point(1, 1)
    p3 = Point(2, 2)
    assert p1 + p2 == p3
