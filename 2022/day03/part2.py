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
    sum = 0
    for line in range(3, len(inp) + 1, 3):
        first = set(inp[line - 3])
        second = set(inp[line - 2])
        third = set(inp[line - 1])

        common = list(first.intersection(second).intersection(third))
        if ord(common[0]) > ord('a'):
            sum += ord(common[0]) - ord('a') + 1
        else:
            sum += ord(common[0]) - ord('A') + 27

    return sum


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 70
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
