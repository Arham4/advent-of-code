import part1


def solution(inp):
    return part1.solution(inp, 40)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 2188189693529
