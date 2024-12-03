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
import part1


def check_safe(nums):
    safe = all([1 <= abs(nums[i - 1] - nums[i]) <= 3 for i in range(1, len(nums))])
    safe &= all([nums[i - 1] > nums[i] for i in range(1, len(nums))]) or all([nums[i - 1] < nums[i] for i in range(1, len(nums))])
    return safe


def solution(inp):
    count = 0
    for line in inp:
        nums = [int(n) for n in line.split(" ")]
        if check_safe(nums):
            count += 1
            continue
        for i in range(len(nums)):
            copy = list(nums)
            copy.pop(i)
            if check_safe(copy):
                count += 1
                break
    return count


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 4
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
