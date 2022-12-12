from typing import List

import part1


def solution(inp: List[str]) -> int:
    grid = [list(row) for row in inp]

    starting_positions = []
    ending_position = (-1, -1)

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == 'S':
                starting_positions.append((row, col))
            elif inp[row][col] == 'a':
                starting_positions.append((row, col))
            elif inp[row][col] == 'E':
                ending_position = (row, col)

    for position in starting_positions:
        grid[position[0]][position[1]] = 'a'
    grid[ending_position[0]][ending_position[1]] = 'z'

    queue = [(position, 0) for position in starting_positions]
    return part1.find_e(inp, ending_position, queue)


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 29
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
