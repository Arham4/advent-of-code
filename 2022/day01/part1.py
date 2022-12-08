from typing import List


def parse_elves(inp: List[str]) -> List[int]:
    elves = []
    curr = 0
    for line in inp:
        if line == '':
            elves.append(curr)
            curr = 0
        else:
            curr += int(line)
    elves.append(curr)
    return elves


def solution(inp: List[str]) -> int:
    return max(parse_elves(inp))


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 24000
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
