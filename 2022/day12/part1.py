from typing import List, Tuple


def find_e(inp: List[str], queue: List[Tuple[Tuple[int, int], int]]) -> int:
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = set()
    while queue:
        instance = queue.pop(0)
        coord = instance[0]

        if coord in visited:
            continue

        letter = inp[coord[0]][coord[1]]
        allowed = [chr(i) for i in range(ord('a'), ord(letter) + 2)]

        if letter == 'E':
            return instance[1]

        visited.add(coord)

        for offset in offsets:
            y = coord[0] + offset[0]
            x = coord[1] + offset[1]

            if y < 0 or y >= len(inp):
                continue
            if x < 0 or x >= len(inp[y]):
                continue

            if letter == 'S' and inp[y][x] == 'a' \
                    or letter == 'S' and inp[y][x] == 'b' \
                    or inp[y][x] == letter \
                    or inp[y][x] in allowed \
                    or letter == 'y' and inp[y][x] == 'E' \
                    or letter == 'z' and inp[y][x] == 'E':
                queue.append(((y, x), instance[1] + 1))

    return -1


def solution(inp: List[str]) -> int:
    starting_position = (-1, -1)

    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == 'S':
                starting_position = (row, col)

    queue = [(starting_position, 0)]
    return find_e(inp, queue)


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 31
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
