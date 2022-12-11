from collections import *
from typing import List

import part1


def solution(inp: List[str]) -> int:
    monkeys = part1.parse_monkeys(inp)
    inspects = defaultdict(lambda: 0)

    supreme_modulus = 1
    for monkey in monkeys:
        supreme_modulus *= int(monkey.test[13:])

    for i in range(10000):
        part1.run_simulation(monkeys, inspects, lambda x: x % supreme_modulus)

    values = sorted(inspects.values())
    return values[-1] * values[-2]


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 2713310158
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
