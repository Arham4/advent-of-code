from typing import List


def solution(inp: List[str]) -> int:
    sum = 0
    for line in range(3, len(inp) + 1, 3):
        first = set(inp[line - 3])
        second = set(inp[line - 2])
        third = set(inp[line - 1])

        common = list(first.intersection(second).intersection(third))
        if ord(common[0]) > ord('a'):
            sum += ord(common[0]) - ord('a') + 1
        else:
            sum += ord(common[0]) - ord('A') + 27

    return sum


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 70
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
