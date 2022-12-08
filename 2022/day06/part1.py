from typing import List


def find_first(line: str, threshold: int) -> int:
    curr = []
    for i in range(len(line)):
        curr.insert(0, line[i])
        if len(curr) == threshold:
            as_set = set(curr)
            if len(as_set) == threshold:
                return i + 1
            curr.pop()
    return -1


def solution(inp: List[str]) -> int:
    return find_first(inp[0], 4)


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 7
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
