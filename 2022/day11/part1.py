from typing import List, DefaultDict, Callable
from collections import defaultdict


class Monkey:
    def __init__(self, number: int):
        self.number = number
        self.items = []
        self.operation = ''
        self.test = ''
        self.if_true = ''
        self.if_false = ''


def parse_monkeys(inp: List[str]) -> List[Monkey]:
    monkeys = []
    number = 0
    current_monkey = Monkey(number)
    for line in inp:
        if line == '':
            monkeys.append(current_monkey)
            number += 1
            current_monkey = Monkey(number)
        elif 'Starting items: ' in line:
            current_monkey.items = [int(item) for item in line.strip()[16:].split(', ')]
        elif 'Operation: ' in line:
            current_monkey.operation = line.strip()[11:]
        elif 'Test: ' in line:
            current_monkey.test = line.strip()[6:]
        elif 'If true: ' in line:
            current_monkey.if_true = line.strip()[9:]
        elif 'If false: ' in line:
            current_monkey.if_false = line.strip()[10:]

    monkeys.append(current_monkey)
    return monkeys


def run_simulation(monkeys: List[Monkey], inspects: DefaultDict[int, int], worry_level_reduction: Callable[[int], int]):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop()
            other = monkey.operation[12:]

            if other == 'old':
                amount = item
            else:
                amount = int(monkey.operation[12:])

            if '*' in monkey.operation:
                value = item * amount
            else:
                value = item + amount

            value = worry_level_reduction(value)

            divisible_amount = int(monkey.test[13:])
            if value % divisible_amount == 0:
                to = int(monkey.if_true[16:])
            else:
                to = int(monkey.if_false[16:])

            monkeys[to].items.append(value)
            inspects[monkey.number] += 1


def solution(inp: List[str]) -> int:
    monkeys = parse_monkeys(inp)
    inspects = defaultdict(lambda: 0)

    for i in range(20):
        run_simulation(monkeys, inspects, lambda x: x // 3)

    values = sorted(inspects.values())
    return values[-1] * values[-2]


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 10605
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
