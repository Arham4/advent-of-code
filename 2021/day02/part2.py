from part1 import sum_term


def solution(inp):
    horizontal = sum_term('forward', inp)

    forward_commands = [0 if 'forward' not in command else int(command.split(' ')[1]) for command in inp]
    depth = sum([(sum_term('down', inp[:i]) - sum_term('up', inp[:i])) * command for i, command in enumerate(forward_commands)])
    return horizontal * depth


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 900
