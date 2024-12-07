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
    pos = (0, 0)
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == "^":
                pos = (y, x)
                break
    direction = 'n'
    next_dir = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
    offsets = {'n': (-1, 0), 'e': (0, 1), 's': (1, 0), 'w': (0, -1)}
    visited = set()
    while 0 <= pos[0] <= len(inp) and 0 <= pos[1] <= len(inp[0]):
        offset = offsets[direction]
        new_y = pos[0] + offset[0]
        new_x = pos[1] + offset[1]
        if new_y < 0 or new_y >= len(inp) or new_x < 0 or new_x >= len(inp[0]):
            break
        if inp[new_y][new_x] == "#":
            direction = next_dir[direction]
            offset = offsets[direction]
            new_y = pos[0] + offset[0]
            new_x = pos[1] + offset[1]
        visited.add(pos)
        pos = (new_y, new_x)
    return len(visited) + 1


def part2(inp):
    pos = (0, 0)
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == "^":
                pos = (y, x)
                break
    direction = 'n'
    next_dir = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
    offsets = {'n': (-1, 0), 'e': (0, 1), 's': (1, 0), 'w': (0, -1)}
    
    def alternate_dimension(inp, direction, pos, visited, culprit):
        while 0 <= pos[0] <= len(inp) and 0 <= pos[1] <= len(inp[0]):
            offset = offsets[direction]
            new_y = pos[0] + offset[0]
            new_x = pos[1] + offset[1]
            if new_y < 0 or new_y >= len(inp) or new_x < 0 or new_x >= len(inp[0]):
                break
            if (pos, direction) in visited:
                return True
            if inp[new_y][new_x] == "#" or (new_y == culprit[0] and new_x == culprit[1]):
                direction = next_dir[direction]
            else:
                visited.add((pos, direction))
                pos = (new_y, new_x)
        return False

    visited = set()
    loops = 0
    while 0 <= pos[0] <= len(inp) and 0 <= pos[1] <= len(inp[0]):
        offset = offsets[direction]
        new_y = pos[0] + offset[0]
        new_x = pos[1] + offset[1]
        new_pos = (new_y, new_x)
        if new_y < 0 or new_y >= len(inp) or new_x < 0 or new_x >= len(inp[0]):
            break
        if inp[new_y][new_x] == "#":
            visited.add(pos)
            direction = next_dir[direction]
        else:
            if new_pos not in visited and alternate_dimension(inp, direction, pos, set(), new_pos):
                loops += 1
            visited.add(pos)
            pos = new_pos
    return loops


def p1_test(examples):
    example = 0
    exp = 41
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 6
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
