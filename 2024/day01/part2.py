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


def solution(inp):
    lefts = defaultdict(lambda: 0)
    rights = defaultdict(lambda: 0)
    for line in inp:
        split = line.split("   ")
        lefts[int(split[0])] += 1
        rights[int(split[1])] += 1

    total = 0
    for line in inp:
        split = line.split("   ")
        num = int(split[0])
        total += num * rights[num]
    return total


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 31
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
