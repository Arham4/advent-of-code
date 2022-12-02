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
    sum = 0
    for line in inp:
        split = line.split(' ')
        if split[0] == 'A':
            if split[1] == 'Y':
                sum += 2 + 6
            elif split[1] == 'X':
                sum += 1 + 3
            else:
                sum += 3 + 0
        elif split[0] == 'B':
            if split[1] == 'Y':
                sum += 2 + 3
            elif split[1] == 'X':
                sum += 1 + 0
            else:
                sum += 3 + 6
        elif split[0] == 'C':
            if split[1] == 'Y':
                sum += 2 + 0
            elif split[1] == 'X':
                sum += 1 + 6
            else:
                sum += 3 + 3
    return sum

def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 15
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
