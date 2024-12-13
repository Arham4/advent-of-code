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
from typing import *

OFFSETS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_region(inp, coord, letter, visited):
    if coord in visited:
        return []
    if coord[0] < 0 or coord[0] >= len(inp) or coord[1] < 0 or coord[1] >= len(inp[0]):
        return []
    if inp[coord[0]][coord[1]] != letter:
        return []
    
    visited.add(coord)
    region = [coord]
    
    for offset_y, offset_x in OFFSETS:
        region.extend(find_region(inp, (coord[0] + offset_y, coord[1] + offset_x), letter, visited))
        
    return region


def part1(inp):
    regions = defaultdict(list)
    filler = 0
    visited = set()
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            letter = inp[y][x]
            region = find_region(inp, (y, x), letter, visited)
            if region:
                regions[(letter, filler)] = region
                filler += 1
    
    price = 0
    for (letter, _), coords in regions.items():
        area = len(coords)
        
        perimeter = 0

        coords_as_a_set = set(coords)
        for y, x in coords:
            for offset_y, offset_x in OFFSETS:
                new_y = y + offset_y
                new_x = x + offset_x
                if new_y < 0 or new_y >= len(inp) or new_x < 0 or new_x >= len(inp[0]) or (new_y, new_x) not in coords_as_a_set:
                    perimeter += 1

        price += area * perimeter
    return price


def find_horizontal_fences(coords):
    horizontal_fences = set()
    for y, x in coords:
        if (y - 1, x) not in coords:
            leftmost_x = x
            while (y, leftmost_x - 1) in coords and (y - 1, leftmost_x - 1) not in coords:
                leftmost_x -= 1
            rightmost_x = x
            while (y, rightmost_x + 1) in coords and (y - 1, rightmost_x + 1) not in coords:
                rightmost_x += 1
            horizontal_fences.add((y, leftmost_x, rightmost_x))

        if (y + 1, x) not in coords:
            leftmost_x = x
            while (y, leftmost_x - 1) in coords and (y + 1, leftmost_x - 1) not in coords:
                leftmost_x -= 1
            rightmost_x = x
            while (y, rightmost_x + 1) in coords and (y + 1, rightmost_x + 1) not in coords:
                rightmost_x += 1
            horizontal_fences.add((y + 1, leftmost_x, rightmost_x))
    return horizontal_fences


def find_vertical_fences(coords):
    vertical_fences = set()
    for y, x in coords:
        if (y, x - 1) not in coords:
            topmost_y = y
            while (topmost_y - 1, x) in coords and (topmost_y - 1, x - 1) not in coords:
                topmost_y -= 1
            bottommost_y = y
            while (bottommost_y + 1, x) in coords and (bottommost_y + 1, x - 1) not in coords:
                bottommost_y += 1
            vertical_fences.add((x, topmost_y, bottommost_y))

        if (y, x + 1) not in coords:
            topmost_y = y
            while (topmost_y - 1, x) in coords and (topmost_y - 1, x + 1) not in coords:
                topmost_y -= 1
            bottommost_y = y
            while (bottommost_y + 1, x) in coords and (bottommost_y + 1, x + 1) not in coords:
                bottommost_y += 1
            vertical_fences.add((x + 1, topmost_y, bottommost_y))
    return vertical_fences


def part2(inp):
    regions = defaultdict(list)
    filler = 0
    visited = set()
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            letter = inp[y][x]
            region = find_region(inp, (y, x), letter, visited)
            if region:
                regions[(letter, filler)] = region
                filler += 1
    
    price = 0
    for (letter, _), coords in regions.items():
        area = len(coords)

        coords_as_a_set = set(coords)

        horizontal_fences = find_horizontal_fences(coords_as_a_set)
        vertical_fences = find_vertical_fences(coords_as_a_set)
        
        sides = len(horizontal_fences) + len(vertical_fences)

        price += area * sides
    return price


def p1_test(examples):
    example = 0
    exp = 1930
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 1
    exp = 80
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 0
    exp = 1206
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
