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
    total = 0
    for line in inp:
        while "mul(" in line:
            index = line.index("mul(")
            end = line[index + 4:]
            index2 = index + 4 + end.index(")")
            nums = line[index:index2].split(",")
            try:
                num1 = int(nums[0].replace("mul(", ""))
                num2 = int(nums[1].replace(")", ""))
                total += num1 * num2
            except Exception:
                pass
            line = line[:index] + line[index + 4:]
    return total


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 161
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
