from functools import reduce


def count_freqs(inp):
    return [reduce(lambda acc, val: acc + (1 if val[i] == '1' else -1), inp, 0) for i in range(len(inp[0]))]


def solution(inp):
    gamma = reduce(lambda acc, val: acc + ('1' if val > 0 else '0'), count_freqs(inp), '')
    epsilon = reduce(lambda acc, val: acc + ('0' if val > 0 else '1'), count_freqs(inp), '')
    return int(gamma, 2) * int(epsilon, 2)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 198
