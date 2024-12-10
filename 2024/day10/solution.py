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


OFFSETS = [(-1,0),(1,0),(0,-1),(0,1)]


def initialize_queue(inp):
    queue = deque()
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '0':
                queue.append(((y, x), int(inp[y][x]), (y, x), set()))
    return queue


def perform_dfs(grid, queue, scores):
    while queue:
        origin, current_height, current_position, visited = queue.pop()
        if current_position in visited:
            continue
        visited = set(visited)
        visited.add(current_position)
        for offset in OFFSETS:
            new_y, new_x = current_position[0] + offset[0], current_position[1] + offset[1]
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                if grid[new_y][new_x] == '.':
                    continue
                new_position = (new_y, new_x)
                new_height = int(grid[new_y][new_x])

                if new_height - current_height == 1:
                    if new_height == 9:
                        if isinstance(scores[origin], list):
                            scores[origin].append(new_position)
                        else:
                            scores[origin].add(new_position)
                    else:
                        queue.append((origin, new_height, new_position, visited))


def calculate_score(scores):
    score = 0
    for num in scores.values():
        score += len(num)
    return score


def part1(inp):
    queue = initialize_queue(inp)
    scores = defaultdict(set)
    perform_dfs(inp, queue, scores)
    return calculate_score(scores)


def part2(inp):
    queue = initialize_queue(inp)
    scores = defaultdict(list)
    perform_dfs(inp, queue, scores)
    return calculate_score(scores)


def p1_test(examples):
    example = 0
    exp = 2
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 4
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    
    example = 2
    exp = 36
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 81
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
