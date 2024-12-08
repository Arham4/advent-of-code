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
    locations = defaultdict(list)

    def is_valid_location(location):
        return 0 <= location[0] < len(inp) and 0 <= location[1] < len(inp[0])

    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] != '.':
                locations[inp[y][x]].append((y, x))
    antinodes = set()
    for _, location_list in locations.items():
        for location in location_list:
            for other_location in location_list:
                if location == other_location:
                    continue
                new_location = (location[0] + (location[0] - other_location[0]), location[1] + (location[1] - other_location[1]))
                if is_valid_location(new_location):
                    antinodes.add(new_location)
    return len(antinodes)


def part2(inp):
    locations = defaultdict(list)

    def is_valid_location(location):
        return 0 <= location[0] < len(inp) and 0 <= location[1] < len(inp[0])

    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] != '.':
                locations[inp[y][x]].append((y, x))
    antinodes = set()
    for _, location_list in locations.items():
        for location in location_list:
            for other_location in location_list:
                if location == other_location:
                    continue
                for i in range(0, len(inp)):
                    new_location = (location[0] + i * (location[0] - other_location[0]), location[1] + i * (location[1] - other_location[1]))
                    if is_valid_location(new_location):
                        antinodes.add(new_location)
                    else:
                        break
    return len(antinodes)


def p1_test(examples):
    example = 0
    exp = 14
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 34
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
