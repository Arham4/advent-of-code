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
    num = 0
    for line in inp:
        split = line.split(',')
        first = split[0].split('-')
        second = split[1].split('-')
        first_range = set(range(int(first[0]), int(first[1]) + 1))
        second_range = set(range(int(second[0]), int(second[1]) + 1))

        if len(first_range.intersection(second_range)) > 0:
            num += 1
            continue
        if len(second_range.intersection(first_range)) > 0:
            num += 1
            continue

    return num


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 4
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
