def solution(inp):
    positions = [int(num) for num in inp[0].split(',')]

    def steps(i, x):
        return abs(positions[i] - x)

    return min(
        [sum([int(steps(i, x) * (steps(i, x) + 1) / 2) for i in range(len(positions))]) for x in range(max(positions))])


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 168
