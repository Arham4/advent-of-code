import part1


def solution(inp):
    return part1.solution(inp, False)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 12
