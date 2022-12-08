from collections import defaultdict
from typing import List


def solution(inp: List[str]) -> str:
    stacks = defaultdict(list)
    moving = False
    for line in inp:
        if line.startswith(' 1') or line == '':
            moving = True
            continue
        if not moving:
            for current_index in range(0, len(line), 4):
                letter = line[current_index:current_index + 4].strip()
                if letter != '':
                    current_group = (current_index // 4) + 1
                    stacks[current_group].insert(0, letter)
        else:
            split = line.split(' ')
            amount = int(split[1])
            from_group = int(split[3])
            to_group = int(split[5])

            for i in range(amount):
                stacks[to_group].append(stacks[from_group].pop())

    output = ''
    for key in sorted(stacks.keys()):
        output += stacks[key][-1].replace('[', '').replace(']', '')
    return output


def result(inp: List[str]) -> str:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 'CMZ'
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
