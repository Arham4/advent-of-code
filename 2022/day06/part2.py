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
    return part1.find_first(inp[0], 14)


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 19
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
