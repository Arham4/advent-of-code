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


def solution(inp):
    count = 0
    for line in inp:
        nums = [int(n) for n in line.split(" ")]
        safe = all([1 <= abs(nums[i - 1] - nums[i]) <= 3 for i in range(1, len(nums))])
        safe &= all([nums[i - 1] > nums[i] for i in range(1, len(nums))]) or all([nums[i - 1] < nums[i] for i in range(1, len(nums))])
        if safe:
            count += 1
    return count

def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 2
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
