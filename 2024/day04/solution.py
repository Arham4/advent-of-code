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
    target = "XMAS"
    rows, cols = len(inp), len(inp[0])
    xmas = 0
    
    def search(y, x, i, direction):
        if i == len(target):
            return 1
        new_y, new_x = y + direction[0], x + direction[1]
        if 0 <= new_y < rows and 0 <= new_x < cols and inp[new_y][new_x] == target[i]:
            return search(new_y, new_x, i + 1, direction)
        return 0

    for y in range(rows):
        for x in range(cols):
            if inp[y][x] == target[0]:
                for combo in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]:
                    xmas += search(y, x, 1, combo)

    return xmas


def part2(inp):
    double_a_locations = set()
    a_locations = set()

    target = "MAS"
    rows, cols = len(inp), len(inp[0])

    def search(y, x, i, direction, a_location):
        if i == len(target):
            if a_location in a_locations:
                double_a_locations.add(a_location)
            else:
                a_locations.add(a_location)
            return
        new_y, new_x = y + direction[0], x + direction[1]
        if 0 <= new_y < rows and 0 <= new_x < cols and inp[new_y][new_x] == target[i]:
            if inp[new_y][new_x] == "A":
                a_location = (new_y, new_x)
            search(new_y, new_x, i + 1, direction, a_location)

    for y in range(rows):
        for x in range(cols):
            if inp[y][x] == target[0]:
                for combo in [(-1, 1), (-1, -1), (1, -1), (1, 1)]:
                    search(y, x, 1, combo, ())
    return len(double_a_locations)


def p1_test(examples):
    example = 0
    exp = 18
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 9
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
