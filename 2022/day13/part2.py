from typing import List
import json

import part1
from part1 import NOT_VALID


def solution(inp: List[str]) -> int:
    original = [json.loads(z) for z in inp if z]

    original.append([[2]])
    original.append([[6]])

    ordered = []

    while original:
        for current in original:
            if all(part1.is_valid(current, other) != NOT_VALID for other in original):
                original.remove(current)
                ordered.append(current)

    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 140
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
