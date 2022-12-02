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
    for line in inp:
        split = line.split(' ')
        if split[0] == 'A':
            if split[1] == 'X':
                sum += 0 + 3
            elif split[1] == 'Y':
                sum += 3 + 1
            else:
                sum += 6 + 2
        elif split[0] == 'B':
            if split[1] == 'X':
                sum += 0 + 1
            elif split[1] == 'Y':
                sum += 3 + 2
            else:
                sum += 6 + 3
        elif split[0] == 'C':
            if split[1] == 'X':
                sum += 0 + 2
            elif split[1] == 'Y':
                sum += 3 + 3
            else:
                sum += 6 + 1
    return sum


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 12
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
