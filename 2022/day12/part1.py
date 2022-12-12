from typing import List, Tuple


def find_e(inp: List[str], goal: Tuple[int, int], queue: List[Tuple[Tuple[int, int], int]]) -> int:
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = set()
    while queue:
        coord, distance = queue.pop(0)

        if coord in visited:
            continue

        if coord == goal:
            return distance

        letter = inp[coord[0]][coord[1]]
        allowed = [chr(i) for i in range(ord('a'), ord(letter) + 2)]

        visited.add(coord)

        for offset in offsets:
            y = coord[0] + offset[0]
            x = coord[1] + offset[1]

            if y < 0 or y >= len(inp):
                continue
            if x < 0 or x >= len(inp[y]):
                continue

            if inp[y][x] in allowed:
                queue.append(((y, x), distance + 1))

    return -1


def solution(inp: List[str]) -> int:
    grid = [list(row) for row in inp]

    starting_position = (-1, -1)
    ending_position = (-1, -1)

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == 'S':
                starting_position = (row, col)
            elif inp[row][col] == 'E':
                ending_position = (row, col)

    grid[starting_position[0]][starting_position[1]] = 'a'
    grid[ending_position[0]][ending_position[1]] = 'z'

    queue = [(starting_position, 0)]
    return find_e(grid, ending_position, queue)


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 31
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
