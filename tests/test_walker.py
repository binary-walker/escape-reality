from walker import walk


def test_walk_balanced():
    assert walk([1, 0, 1, 0])[-1] == 0


def test_walk_right():
    assert walk([1, 1, 1])[-1] == 3
