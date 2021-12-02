def solution(inp):
    horizontal = sum(map(lambda v: int(v.split(' ')[1]), filter(lambda v: "forward" in v, inp)))
    downs = sum(map(lambda v: int(v.split(' ')[1]), filter(lambda v: "down" in v, inp)))
    ups = sum(map(lambda v: int(v.split(' ')[1]), filter(lambda v: "up" in v, inp)))
    return horizontal * (downs - ups)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 150
