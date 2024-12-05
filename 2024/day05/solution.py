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


def part1(inp):
    dependencies = defaultdict(list)
    parsing = False
    total = 0
    for i in range(len(inp)):
        line = inp[i]
        if line == "":
            parsing = True
            continue
        if not parsing:
            split = line.split("|")
            dependencies[int(split[0])].append(int(split[1]))
        else:
            valid, points = is_valid(dependencies, line)
            if valid:
                total += points
    return total


def is_valid(dependencies, line):
    visited = set()
    split = [int(n) for n in line.split(",")]
    invalid = False
    for num in split:
        for deps in dependencies[num]:
            if deps in visited:
                invalid = True
                break
        if invalid:
            break
        visited.add(num)
    return (not invalid, int(split[len(split) // 2]))


def part2(inp):
    dependencies = defaultdict(list)
    parsing = False
    total = 0

    def reorder(line, first_pass):
        visited = set()
        split = [int(n) for n in line.split(",")]
        ideal = list(split)
        invalid = False
        for num in split:
            for deps in dependencies[num]:
                if deps in visited:
                    ideal.pop(ideal.index(num))
                    ideal.insert(ideal.index(deps), num)
                    invalid = True
            visited.add(num)
        if first_pass and not invalid:
            return 0
        valid, num = is_valid(dependencies, line)
        if valid:
            return int(ideal[len(ideal) // 2])
        return reorder(",".join([str(x) for x in ideal]), False)

    for i in range(len(inp)):
        line = inp[i]
        if line == "":
            parsing = True
            continue
        if not parsing:
            split = line.split("|")
            dependencies[int(split[0])].append(int(split[1]))
        else:
            total += reorder(line, True)
    return total


def p1_test(examples):
    example = 0
    exp = 143
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 0
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 123
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 3
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
