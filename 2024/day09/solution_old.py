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
import time


def part1(inp):
    spaces = {}
    file_number = 0
    for i in range(0, len(inp[0]), 2):
        spaces[file_number] = [tuple([str(file_number)])] * int(inp[0][i])
        if i + 1 < len(inp[0]):
            spaces[file_number] = spaces[file_number] + [tuple('.')] * int(inp[0][i + 1])
        file_number += 1

    keys = list(spaces.keys())
    left = 0
    right = keys[len(keys) - 1]
    while left < right:
        left_spaces = spaces[left]
        right_spaces = spaces[right]

        left_empty = left_spaces.index(tuple('.')) if tuple('.') in left_spaces else -1
        if left_empty == -1:
            left += 1
            continue

        quit = False
        for i in range(len(right_spaces) - 1, -1, -1):
            if right_spaces[i] == tuple('.'):
                continue
            left_spaces[left_empty] = right_spaces[i]
            right_spaces[i] = tuple('.')
            left_empty += 1
            if left_empty >= len(left_spaces):
                left += 1
                quit = True
                break
        if quit:
            continue

        spaces[left] = left_spaces
        spaces[right] = right_spaces
        right -= 1
    
    checksum = 0
    position = 0
    for key in keys:
        for space in spaces[key]:
            if space == tuple('.'):
                continue
            checksum += position * int(space[0])
            position += 1
    return checksum


def part2(inp):
    spaces = {}
    file_number = 0
    for i in range(0, len(inp[0]), 2):
        spaces[file_number] = [tuple([str(file_number)])] * int(inp[0][i])
        if i + 1 < len(inp[0]):
            spaces[file_number] = spaces[file_number] + [tuple('.')] * int(inp[0][i + 1])
        file_number += 1

    keys = list(spaces.keys())
    right = keys[len(keys) - 1]
    cum1 = 0
    cum2 = 0
    last_output = right

    while right > 0:
        if last_output % 100 == 0:
            cum1avg = cum1 / 100
            cum2avg = cum2 / 100
            print(last_output, "(average time:", cum1avg, "seconds for loop 1", cum2avg, "seconds for loop 2, ETA:", (cum1avg + cum2avg) * (len(keys) - 1), "seconds)")
            cum1 = 0
            cum2 = 0

        right_spaces = spaces[right]
        right_nonfree_space = right_spaces.count(tuple([str(right)]))
        left = None
        s = time.time()
        for key in keys:
            if keys.index(key) >= keys.index(right):
                break
            left_free_space = spaces[key].count(tuple('.'))
            if left_free_space >= right_nonfree_space:
                left = key
                break
        cum1 += time.time() - s
        if left is None:
            last_output -= 1
            right -= 1
            continue

        left_spaces = spaces[left]

        right_index = right_spaces.index(tuple([str(right)]))
        s = time.time()
        while tuple('.') in left_spaces and right_index >= 0:
            left_spaces[left_spaces.index(tuple('.'))] = right_spaces[right_index]
            right_spaces[right_index] = tuple('.')
            right_index = right_spaces.index(tuple([str(right)])) if tuple([str(right)]) in right_spaces else -1
        cum2 += time.time() - s

        spaces[left] = left_spaces
        spaces[right] = right_spaces
        last_output -= 1
        right -= 1
    
    checksum = 0
    position = -1
    for key in keys:
        for space in spaces[key]:
            position += 1
            if space == tuple('.'):
                continue
            checksum += position * int(space[0])
    return checksum


def p1_test(examples):
    example = 0
    exp = 60
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 1928
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 2
    exp = 10
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 2858
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
