from typing import List
import part1


def solution(inp: List[str]):
    head_position = [0, 0]
    tail_positions = [[0, 0] for i in range(9)]

    visited = set()

    for line in inp:
        split = line.split(' ')
        direction = split[0]
        amount = int(split[1])

        for i in range(amount):
            part1.move_head(head_position, direction)
            part1.move_tail(head_position, tail_positions[0])

            for x in range(1, 9):
                part1.move_tail(tail_positions[x - 1], tail_positions[x])

            visited.add(tuple(tail_positions[8]))

    return len(visited)


def result(inp: List[str]):
    return solution(inp)


def test(examples: List[List[str]]):
    example = 0
    exp = 1
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 36
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
