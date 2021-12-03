import part1


def solution(inp):
    oxy_list = inp.copy()
    index = 0
    while len(oxy_list) != 1:
        freqs = part1.count_freqs(oxy_list)
        oxy_list = [x for x in oxy_list if freqs[index] >= 0 and x[index] == '1' or freqs[index] < 0 and x[index] == '0']
        index += 1
    co2_list = inp.copy()
    index = 0
    while len(co2_list) != 1:
        freqs = part1.count_freqs(co2_list)
        co2_list = [x for x in co2_list if freqs[index] < 0 and x[index] == '1' or freqs[index] >= 0 and x[index] == '0']
        index += 1
    return int(oxy_list[0], 2) * int(co2_list[0], 2)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 230
