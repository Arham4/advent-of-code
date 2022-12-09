from typing import List


def move_head(head: List[int], direction: str):
    if direction == 'R':
        head[0] += 1
    elif direction == 'L':
        head[0] -= 1
    elif direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1


def move_tail(head: List[int], tail: List[int]):
    magnitude = [head[0] - tail[0], head[1] - tail[1]]

    if abs(magnitude[0]) == 2 or abs(magnitude[1]) == 2:
        tail[0] += magnitude[0] // max(1, abs(magnitude[0]))
        tail[1] += magnitude[1] // max(1, abs(magnitude[1]))


def solution(inp: List[str]):
    head = [0, 0]
    tail = [0, 0]

    visited = set()

    for line in inp:
        split = line.split(' ')
        direction = split[0]
        amount = int(split[1])

        for i in range(amount):
            move_head(head, direction)
            move_tail(head, tail)
            visited.add(tuple(tail))

    return len(visited)


def result(inp: List[str]):
    return solution(inp)


def test(examples: List[List[str]]):
    example = 0
    exp = 13
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
