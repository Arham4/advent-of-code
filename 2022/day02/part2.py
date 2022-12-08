from typing import List


def solution(inp: List[str]) -> int:
    sum = 0
    for line in inp:
        split = line.split(' ')
        if split[0] == 'A':
            if split[1] == 'X':
                sum += 0 + 3
            elif split[1] == 'Y':
                sum += 3 + 1
            else:
                sum += 6 + 2
        elif split[0] == 'B':
            if split[1] == 'X':
                sum += 0 + 1
            elif split[1] == 'Y':
                sum += 3 + 2
            else:
                sum += 6 + 3
        elif split[0] == 'C':
            if split[1] == 'X':
                sum += 0 + 2
            elif split[1] == 'Y':
                sum += 3 + 3
            else:
                sum += 6 + 1
    return sum


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]):
    example = 0
    exp = 12
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
