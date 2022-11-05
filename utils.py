def add(*tuples: (float, float)) -> (float, float):
    for item in tuples:
        assert len(item) == 2
    return sum([t[0] for t in tuples]), sum([t[1] for t in tuples])


def flip_vertically(vector: (float, float)) -> (float, float):
    assert len(vector) == 2
    return vector[0], -vector[1]


def flip_horizontally(vector: (float, float)) -> (float, float):
    assert len(vector) == 2
    return -vector[0], vector[1]
