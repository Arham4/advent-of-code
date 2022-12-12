from typing import List

import part1


def solution(inp: List[str]) -> int:
    starting_positions = []
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == 'S':
                starting_positions.append((row, col))
            elif inp[row][col] == 'a':
                starting_positions.append((row, col))

    queue = [(position, 0) for position in starting_positions]
    return part1.find_e(inp, queue)


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 29
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
