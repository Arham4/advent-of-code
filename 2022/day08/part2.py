from typing import List
import part1


def solution(inp: List[str]) -> int:
    scores = {}
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            visibility_above = part1.is_visible_above(inp, y, x)
            if False in visibility_above:
                up_value = visibility_above.index(False) + 1
            else:
                up_value = len(visibility_above)

            visibility_left = part1.is_visible_on_left(inp, y, x)
            if False in visibility_left:
                left_value = visibility_left.index(False) + 1
            else:
                left_value = len(visibility_left)

            visibility_right = part1.is_visible_on_right(inp, y, x)
            if False in visibility_right:
                right_value = visibility_right.index(False) + 1
            else:
                right_value = len(visibility_right)

            visibility_below = part1.is_visible_below(inp, y, x)
            if False in visibility_below:
                down_value = visibility_below.index(False) + 1
            else:
                down_value = len(visibility_below)

            scores[(y, x)] = up_value * left_value * right_value * down_value
    return max(scores.values())


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 8
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
