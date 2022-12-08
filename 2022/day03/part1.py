from typing import List


def solution(inp: List[str]) -> int:
    sum = 0
    for line in inp:
        first = set(line[:len(line) // 2])
        second = set(line[len(line) // 2:])

        common = list(first.intersection(second))
        if ord(common[0]) > ord('a'):
            sum += ord(common[0]) - ord('a') + 1
        else:
            sum += ord(common[0]) - ord('A') + 27
    return sum


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 157
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
