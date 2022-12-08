from typing import List


def solution(inp: List[str]) -> int:
    num = 0
    for line in inp:
        split = line.split(',')
        first = split[0].split('-')
        second = split[1].split('-')
        first_range = set(range(int(first[0]), int(first[1]) + 1))
        second_range = set(range(int(second[0]), int(second[1]) + 1))

        if len(first_range.intersection(second_range)) > 0:
            num += 1
            continue
        if len(second_range.intersection(first_range)) > 0:
            num += 1
            continue

    return num


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 4
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
