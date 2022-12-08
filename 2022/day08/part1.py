from typing import List


def is_visible_above(inp: List[str], y: int, x: int) -> List[bool]:
    return [int(inp[i][x]) < int(inp[y][x]) for i in range(y - 1, -1, -1)]


def is_visible_on_left(inp: List[str], y: int, x: int) -> List[bool]:
    return [int(inp[y][i]) < int(inp[y][x]) for i in range(x - 1, -1, -1)]


def is_visible_on_right(inp: List[str], y: int, x: int) -> List[bool]:
    return [int(inp[y][i]) < int(inp[y][x]) for i in range(x + 1, len(inp[y]))]


def is_visible_below(inp: List[str], y: int, x: int) -> List[bool]:
    return [int(inp[i][x]) < int(inp[y][x]) for i in range(y + 1, len(inp))]


def solution(inp: List[str]) -> int:
    visible = {}
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            visible_up = all(is_visible_above(inp, y, x))
            visible_left = all(is_visible_on_left(inp, y, x))
            visible_right = all(is_visible_on_right(inp, y, x))
            visible_down = all(is_visible_below(inp, y, x))

            visible[(y, x)] = visible_up or visible_left or visible_right or visible_down
    return sum(visible.values())


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 21
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
