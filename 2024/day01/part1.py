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
    lefts = []
    rights = []
    for line in inp:
        split = line.split("   ")
        lefts.append(int(split[0]))
        rights.append(int(split[1]))
    lefts = sorted(lefts)
    rights = sorted(rights)
    total = 0
    for i in range(len(lefts)):
        total += abs(lefts[i] - rights[i])
    return total

def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 11
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
