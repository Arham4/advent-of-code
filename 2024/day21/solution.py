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


def bfs(grid, start, goal, avoid):
    visited = set()
    queue = deque([(start, "")])
    paths = defaultdict(list)
    while queue:
        (y, x), path = queue.popleft()
        if grid[y][x] == goal:
            path = path + "A"
            paths[len(path)].append((path, (y, x)))
            continue
        visited.add((y, x))
        for symbol, dy, dx in [(">", 0, 1), ("<", 0, -1), ("v", 1, 0), ("^", -1, 0)]:
            new_y, new_x = y + dy, x + dx
            new_pos = (new_y, new_x)
            if new_pos == avoid:
                continue
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                if new_pos not in visited:
                    queue.append((new_pos, path + symbol))
    return paths[min(paths.keys())]


def get_paths(start, numeric, cache):
    queue = deque([(start, 0, "")])
    shortest_length = float('inf')
    shortest = set()
    while queue:
        pos, target_index, current_path = queue.popleft()
        if target_index == len(numeric):
            if len(current_path) < shortest_length:
                shortest_length = len(current_path)
                shortest = {current_path}
            elif len(current_path) == shortest_length:
                shortest.add(current_path)
            continue

        paths = cache[(pos, numeric[target_index])]
        for path, end in paths:
            if len(current_path + path) <= shortest_length:
                queue.append((end, target_index + 1, current_path + path))
    return shortest


def get_robot_paths(start, code, cache, num_robots):
    if num_robots == 1:
        return get_paths(start, code, cache)

    robot_paths = defaultdict(list)
    initial_paths = get_paths(start, code, cache)

    for path in initial_paths:
        sub_robot_paths = get_robot_paths(start, path, cache, num_robots - 1)
        for sub_path in sub_robot_paths:
            robot_paths[len(sub_path)].append(sub_path)
    
    return robot_paths


def precompute_paths(grid, avoid):
    cache = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y == avoid[0] and x == avoid[1]:
                continue
            for oy in range(len(grid)):
                for ox in range(len(grid[oy])):
                    if oy == avoid[0] and ox == avoid[1]:
                        continue
                    optimal_paths = bfs(grid, (y, x), grid[oy][ox], avoid)
                    cache[((y, x), grid[oy][ox])] = optimal_paths
    return cache


def part1(inp):
    direction_grid = [
        "_^A",
        "<v>",
    ]
    numeric_grid = [
        "789",
        "456",
        "123",
        "_0A",
    ]
    direction_cache = precompute_paths(direction_grid, (0, 0))
    numeric_cache = precompute_paths(numeric_grid, (3, 0))
    total_complexity = 0
    for code in inp:
        numeric_path = get_paths((3, 2), code, numeric_cache)
        robot1_paths = defaultdict(list)
        for numpath in numeric_path:
            robot1_paths.update(get_robot_paths((0, 2), numpath, direction_cache, 2))
        numeric_part = int(code[:3])
        shortest = min(robot1_paths.keys())
        print(code, "-", shortest, "*", numeric_part)
        total_complexity += shortest * numeric_part
    return total_complexity


def part2(inp):
    direction_grid = [
        "_^A",
        "<v>",
    ]
    numeric_grid = [
        "789",
        "456",
        "123",
        "_0A",
    ]
    direction_cache = precompute_paths(direction_grid, (0, 0))
    numeric_cache = precompute_paths(numeric_grid, (3, 0))
    total_complexity = 0
    for code in inp:
        numeric_path = get_paths((3, 2), code, numeric_cache)
        robot1_paths = defaultdict(list)
        for numpath in numeric_path:
            robot1_paths.update(get_robot_paths((0, 2), numpath, direction_cache, 25))
        numeric_part = int(code[:3])
        shortest = min(robot1_paths.keys())
        print(code, "-", shortest, "*", numeric_part)
        total_complexity += shortest * numeric_part
    return total_complexity


def p1_test(examples):
    example = 0
    exp = 126384
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    '''
    example = 0
    exp = 0
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    '''
