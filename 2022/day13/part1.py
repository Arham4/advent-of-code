from typing import List
import json

VALID = 1
NOT_VALID = 0
PASS = -1


def is_valid(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return VALID
        elif right < left:
            return NOT_VALID

        return PASS
    elif isinstance(left, list) and isinstance(right, list):
        for left_value, right_value in zip(left, right):
            valid = is_valid(left_value, right_value)
            if valid == VALID:
                return VALID
            elif valid == NOT_VALID:
                return NOT_VALID

        if len(left) < len(right):
            return VALID
        elif len(right) < len(left):
            return NOT_VALID

        return PASS
    elif isinstance(left, int):
        left = [left]
        return is_valid(left, right)
    elif isinstance(right, int):
        right = [right]
        return is_valid(left, right)
    return NOT_VALID


def solution(inp: List[str]) -> int:
    sum = 0
    pair = 1

    for i in range(0, len(inp), 3):
        left = json.loads(inp[i])
        right = json.loads(inp[i+1])

        valid = is_valid(left, right)

        if valid == PASS:
            pair += 1
            continue

        if valid == VALID:
            sum += pair

        pair += 1

    return sum


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 13
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
