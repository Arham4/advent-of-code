import part1


def solution(inp):
    horizontal = 0
    depth = 0
    aim = 0
    for line in inp:
        split = line.split(" ")
        if "forward" in line:
            horizontal += int(split[1])
            depth += aim * int(split[1])
        elif "down" in line:
            aim += int(split[1])
        elif "up" in line:
            aim -= int(split[1])
    return horizontal * depth


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 900
