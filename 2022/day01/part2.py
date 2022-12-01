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
    elves = part1.parse_elves(inp)
    elves.sort()
    return elves[-1] + elves[-2] + elves[-3]


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 45000
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
