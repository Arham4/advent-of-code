import collections
from collections import *
import functools
from functools import *
import itertools
from itertools import *
import math
from math import *
import json
from json import *
import re
from re import *
import heapq
from heapq import *


def create_stones_counter(inp):
    return Counter(inp[0].split(' '))


def blink(stones_counter):
    new_counter = Counter()
    for stones in stones_counter.keys():
        if stones == "0":
            new_counter["1"] += stones_counter[stones]
        elif len(stones) % 2 != 0:
            new_counter[str(int(stones) * 2024)] += stones_counter[stones]
        elif len(stones) % 2 == 0:
            mid = len(stones) // 2
            left_stone = str(int(stones[:mid]))
            right_stone = str(int(stones[mid:]))
            new_counter[left_stone] += stones_counter[stones]
            new_counter[right_stone] += stones_counter[stones]
    return new_counter


def blink_multiple_times(stones_counter, blinks):
    for _ in range(blinks):
        stones_counter = blink(stones_counter)
    return stones_counter


def part1(inp):
    stones_counter = create_stones_counter(inp)
    stones_counter = blink_multiple_times(stones_counter, 25)
    return stones_counter.total()


def part2(inp):
    stones_counter = create_stones_counter(inp)
    stones_counter = blink_multiple_times(stones_counter, 75)
    return stones_counter.total()


def p1_test(examples):
    example = 0
    exp = 55312
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    '''
    example = 0
    exp = 0
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    '''
