def summation(num):
    return int(num * (num + 1) / 2)


def solution(inp):
    positions = [int(num) for num in inp[0].split(',')]
    return min([sum([summation(abs(positions[i] - x)) for i in range(len(positions))]) for x in range(max(positions))])


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 168
