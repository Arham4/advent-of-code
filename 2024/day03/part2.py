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
    total = 0
    enabled = True
    for line in inp:
        for command in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
            if command == "don't()":
                enabled = False
            elif command == "do()":
                enabled = True
            elif enabled:
                split = command.replace("mul(", "").replace(")", "").split(",")
                total += int(split[0]) * int(split[1])
    return total

'''
may nobody ever be so cursed to inflict a plague upon their eyes by seeing this code...

def solution(inp):
    total = 0
    line = "".join(inp)
    while "mul(" in line:
        index = line.index("mul(")
        do_index = 0
        dont_index = 0
        end = line[index + 4:]
        try:
            do_index = line[:index].rfind("do()")
        except Exception:
            pass
        try:
            dont_index = line[:index].rfind("don't()")
        except Exception:
            pass
        index2 = index + 4 + end.index(")")
        nums = line[index + 4:index2].split(",")
        enabled = True if (do_index == -1 and dont_index == -1) or do_index > dont_index else False
        get_inner1 = False
        get_inner2 = False
        try:
            if "mul(" in nums[0]:
                get_inner1 = True
                raise Exception
            if "mul(" in nums[1]:
                get_inner2 = True
                raise Exception
            num1 = int(nums[0])
            num2 = int(nums[1].replace(")", ""))
            if enabled:
                total += num1 * num2
        except Exception:
            pass
        if get_inner1:
            index2 = index + nums[0].index("mul(")
        if get_inner2:
            index2 = index + len(nums[0]) + nums[1].index("mul(")
        if enabled:
            line = "do()" + line[index2 + 1:]
        else:
            line = "don't()" + line[index2 + 1:]
    return total
'''


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 48
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 121
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 2
    exp = 123
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
