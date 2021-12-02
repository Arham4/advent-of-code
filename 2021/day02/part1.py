def sum_term(term, inp):
    return sum(map(lambda v: int(v.split(' ')[1]), filter(lambda v: term in v, inp)))


def solution(inp):
    horizontal = sum_term('forward', inp)
    downs = sum_term('down', inp)
    ups = sum_term('up', inp)
    return horizontal * (downs - ups)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 150
