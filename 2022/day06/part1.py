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


def find_first(line, threshold):
    curr = []
    for i in range(len(line)):
        curr.insert(0, line[i])
        if len(curr) == threshold:
            as_set = set(curr)
            if len(as_set) == threshold:
                return i + 1
            curr.pop()
    return -1


def solution(inp):
    return find_first(inp[0], 4)


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 7
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
