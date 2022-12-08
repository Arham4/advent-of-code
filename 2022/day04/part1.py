from typing import List


def solution(inp: List[str]) -> int:
    num = 0
    for line in inp:
        split = line.split(',')
        first = split[0].split('-')
        second = split[1].split('-')
        first_range = set(range(int(first[0]), int(first[1]) + 1))
        second_range = set(range(int(second[0]), int(second[1]) + 1))

        first_intersect = first_range.intersection(second_range)
        if len(first_intersect) == len(first_range):
            num += 1
            continue
        second_intersect = second_range.intersection(first_range)
        if len(second_intersect) == len(second_range):
            num += 1
            continue

    return num


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 2
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
