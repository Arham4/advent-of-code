def solution(inp):
    entries = [[segment.split(' | ')[0].split(' '), segment.split(' | ')[1].split(' ')] for segment in inp]
    identified = 0
    for entry in entries:
        left = entry[0]
        right = entry[1]

        lengths = {}
        for word in left:
            if len(word) in lengths:
                lengths[len(word)] += 1
            else:
                lengths[len(word)] = 1

        for word in right:
            if len(word) in lengths and lengths[len(word)] == 1:
                identified += 1

    return identified


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 26
