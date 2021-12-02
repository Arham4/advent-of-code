def solution(inp):
    horizontal = 0
    depth = 0
    for line in inp:
        split = line.split(" ")
        if "forward" in line:
            horizontal += int(split[1])
        elif "down" in line:
            depth += int(split[1])
        elif "up" in line:
            depth -= int(split[1])
    return horizontal * depth


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 150
