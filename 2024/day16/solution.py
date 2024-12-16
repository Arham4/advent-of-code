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
    start = None
    destination = None
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == 'S':
                start = (y, x, 0)
            elif inp[y][x] == 'E':
                destination = (y, x)
            if start and destination:
                break
        if start and destination:
            break
    
    offset_y = [0, 1, 0, -1]
    offset_x = [1, 0, -1, 0]

    def is_valid(y, x, direction):
        if direction == -1:
            direction = len(offset_y) - 1
        direction = direction % len(offset_y)
        dest_y = y + offset_y[direction]
        dest_x = x + offset_x[direction]
        return inp[dest_y][dest_x] != '#', (dest_y, dest_x, direction)
    
    visited_scores = {}
    queue = deque([(start, 0)])
    min_score = float('inf')

    while queue:
        state, score = queue.popleft()
        y, x, direction = state

        if state in visited_scores and score >= visited_scores[state]:
            continue

        visited_scores[state] = score

        if (y, x) == destination:
            min_score = min(min_score, score)
            continue

        valid, new_position = is_valid(y, x, direction)
        if valid:
            new_score = score + 1
            if new_position not in visited_scores or new_score < visited_scores[new_position]:
                queue.append((new_position, new_score))
        
        valid, new_position = is_valid(y, x, direction + 1)
        if valid:
            new_score = score + 1001
            if new_position not in visited_scores or new_score < visited_scores[new_position]:
                queue.append((new_position, new_score))
        
        valid, new_position = is_valid(y, x, direction - 1)
        if valid:
            new_score = score + 1001
            if new_position not in visited_scores or new_score < visited_scores[new_position]:
                queue.append((new_position, new_score))

    return min_score


def part2(inp):
    start = None
    destination = None
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == 'S':
                start = (y, x, 0)
            elif inp[y][x] == 'E':
                destination = (y, x)
            if start and destination:
                break
        if start and destination:
            break
    
    offset_y = [0, 1, 0, -1]
    offset_x = [1, 0, -1, 0]

    def is_valid(y, x, direction):
        if direction == -1:
            direction = len(offset_y) - 1
        direction = direction % len(offset_y)
        dest_y = y + offset_y[direction]
        dest_x = x + offset_x[direction]
        return inp[dest_y][dest_x] != '#', (dest_y, dest_x, direction)
    
    visited_scores = {}
    queue = deque([(start, 0, [])])
    scores = []

    while queue:
        state, score, path = queue.popleft()
        y, x, direction = state
        
        path = list(path)
        path.append((y, x))

        if state in visited_scores and score > visited_scores[state]:
            continue

        visited_scores[state] = score

        if (y, x) == destination:
            scores.append((score, path))
            continue

        valid, new_position = is_valid(y, x, direction)
        if valid:
            new_score = score + 1
            if new_position not in visited_scores or new_score <= visited_scores[new_position]:
                queue.append((new_position, new_score, path))
        
        valid, new_position = is_valid(y, x, direction + 1)
        if valid:
            new_score = score + 1001
            if new_position not in visited_scores or new_score <= visited_scores[new_position]:
                queue.append((new_position, new_score, path))
        
        valid, new_position = is_valid(y, x, direction - 1)
        if valid:
            new_score = score + 1001
            if new_position not in visited_scores or new_score <= visited_scores[new_position]:
                queue.append((new_position, new_score, path))

    scores = sorted(scores)
    min_score = scores[0][0]
    tiles = set()
    for score, path in scores:
        if score > min_score:
            break
        tiles.update(path)
    return len(tiles)


def p1_test(examples):
    example = 0
    exp = 7036
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 11048
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 45
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 64
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
