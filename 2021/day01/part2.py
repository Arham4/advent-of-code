import part1


def result(inp):
    return part1.result2(inp, 3)


def test(example_inp):
    assert result(example_inp) == 5
