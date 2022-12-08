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
    scores = {}
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            not_visible_above = part1.not_visible_above(inp, y, x)
            if True in not_visible_above:
                up_value = not_visible_above.index(True) + 1
            else:
                up_value = len(not_visible_above)

            not_visible_on_left = part1.not_visible_on_left(inp, y, x)
            if True in not_visible_on_left:
                left_value = not_visible_on_left.index(True) + 1
            else:
                left_value = len(not_visible_on_left)

            not_visible_on_right = part1.not_visible_on_right(inp, y, x)
            if True in not_visible_on_right:
                right_value = not_visible_on_right.index(True) + 1
            else:
                right_value = len(not_visible_on_right)

            not_visible_below = part1.not_visible_below(inp, y, x)
            if True in not_visible_below:
                down_value = not_visible_below.index(True) + 1
            else:
                down_value = len(not_visible_below)

            scores[(y, x)] = up_value * left_value * right_value * down_value
    return max(scores.values())


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 8
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
