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


def parse_elves(inp):
    elves = []
    curr = 0
    for line in inp:
        if line == '':
            elves.append(curr)
            curr = 0
        else:
            curr += int(line)
    elves.append(curr)
    return elves


def solution(inp):
    return max(parse_elves(inp))


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 24000
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
