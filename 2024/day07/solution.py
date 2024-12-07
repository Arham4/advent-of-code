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


def part1(inp):
    total = 0
    for line in inp:
        eval = line.split(": ")
        target = int(eval[0])
        nums = [int(x) for x in eval[1].split(" ")]
        queue = [(nums[0], 1)]
        while queue:
            current, next_index = queue.pop()
            if current == target and next_index == len(nums):
                total += current
                break
            
            if next_index >= len(nums):
                continue

            queue.append((current + nums[next_index], next_index + 1))
            queue.append((current * nums[next_index], next_index + 1))
    return total


def part2(inp):
    total = 0
    for line in inp:
        eval = line.split(": ")
        target = int(eval[0])
        nums = [int(x) for x in eval[1].split(" ")]
        queue = [(nums[0], 1)]
        while queue:
            current, next_index = queue.pop()
            if current == target and next_index == len(nums):
                total += current
                break
            
            if next_index >= len(nums):
                continue

            queue.append((current + nums[next_index], next_index + 1))
            queue.append((current * nums[next_index], next_index + 1))
            queue.append((int(str(current) + str(nums[next_index])), next_index + 1))
    return total


def p1_test(examples):
    example = 0
    exp = 3749
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 11387
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
