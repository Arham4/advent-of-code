from typing import List


def solution(inp: List[str]) -> int:
    x = 1
    cycles = 0
    summed = 0
    for line in inp:
        if line == 'noop':
            cycles += 1

            if cycles % 40 == 20:
                summed += cycles * x

        else:
            amount = int(line.split(' ')[1])

            for i in range(2):
                cycles += 1
                if cycles % 40 == 20:
                    summed += cycles * x

            x += amount
    return summed


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 13140
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
