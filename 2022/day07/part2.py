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
    paths = part1.populate_paths(inp)

    sizes = []
    for path in paths:
        size = part1.find_size_of_directory(paths, path)
        sizes.append(size)

    sizes.sort()

    used = sizes.pop()
    unused = 70000000 - used
    limit = 30000000
    index = -1
    for i in range(-1, -len(sizes), -1):
        if unused + sizes[i] >= limit:
            index = i
    return sizes[index]


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 24933642
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
