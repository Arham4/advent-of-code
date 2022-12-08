from typing import List
import part1


def solution(inp: List[str]) -> int:
    elves = part1.parse_elves(inp)
    elves.sort()
    return elves[-1] + elves[-2] + elves[-3]


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 45000
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
