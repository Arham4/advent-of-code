def sum_term(term, inp):
    return sum([command.split(' ')[1] for command in [command for command in inp if term in command]])


def solution(inp):
    horizontal = sum_term('forward', inp)
    downs = sum_term('down', inp)
    ups = sum_term('up', inp)
    return horizontal * (downs - ups)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 150
