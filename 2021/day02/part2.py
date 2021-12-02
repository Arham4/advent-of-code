import part1


def solution(inp):
    horizontal = part1.sum_term('forward', inp)
    depth = sum(map(lambda i_v: 0 if 'forward' not in i_v[1] else (part1.sum_term('down', inp[:i_v[0]]) - part1.sum_term('up', inp[:i_v[0]])) * int(i_v[1].split(' ')[1]), enumerate(inp)))
    return horizontal * depth


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 900
