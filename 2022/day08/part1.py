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


def not_visible_above(inp, y, x):
    return [int(inp[i][x]) >= int(inp[y][x]) for i in range(y - 1, -1, -1)]


def not_visible_on_left(inp, y, x):
    return [int(inp[y][i]) >= int(inp[y][x]) for i in range(x - 1, -1, -1)]


def not_visible_on_right(inp, y, x):
    return [int(inp[y][i]) >= int(inp[y][x]) for i in range(x + 1, len(inp[y]))]


def not_visible_below(inp, y, x):
    return [int(inp[i][x]) >= int(inp[y][x]) for i in range(y + 1, len(inp))]


def solution(inp):
    visible = {}
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            visible_up = not any(not_visible_above(inp, y, x))
            visible_left = not any(not_visible_on_left(inp, y, x))
            visible_right = not any(not_visible_on_right(inp, y, x))
            visible_down = not any(not_visible_below(inp, y, x))

            visible[(y, x)] = visible_up or visible_left or visible_right or visible_down
    return sum(visible.values())


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 21
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
