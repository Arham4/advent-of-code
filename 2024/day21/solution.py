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


@cache
def get_robot_paths(sequence, num_robots, dir_sequences, dir_lengths):
    if num_robots == 1:
        return sum(get_length(dir_lengths, x, y) for x, y in zip("A" + sequence, sequence))
    
    length = 0
    for x, y in zip("A" + sequence, sequence):
        subsequences = get_sequence(dir_sequences, x, y)
        length += min(get_robot_paths(subsequence, num_robots - 1, dir_sequences, dir_lengths) for subsequence in subsequences)
    return length


def precompute_paths(grid, avoid):
    sequences = {}
    lengths = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y == avoid[0] and x == avoid[1]:
                continue
            for oy in range(len(grid)):
                for ox in range(len(grid[oy])):
                    if oy == avoid[0] and ox == avoid[1]:
                        continue
                    optimal_paths = bfs(grid, (y, x), grid[oy][ox], avoid)
                    if optimal_paths:
                        sequences[(grid[y][x], grid[oy][ox])] = tuple(p[0] for p in optimal_paths)
                        lengths[(grid[y][x], grid[oy][ox])] = len(optimal_paths[0][0])
    seqs = tuple((k, v) for k, v in sorted(sequences.items()))
    lens = tuple((k, v) for k, v in sorted(lengths.items()))
    return seqs, lens


def get_sequence(sequences, start, end):
    for (s, e), paths in sequences:
        if (s, e) == (start, end):
            return paths
    return None


def get_length(sequences, start, end):
    for (s, e), length in sequences:
        if (s, e) == (start, end):
            return length
    return None


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
        possible_sequences = []
        for combination in product(*[get_sequence(numeric_cache[0], x, y) for x, y in zip("A" + code, code)]):
            possible_sequences.append("".join(combination))
        
        min_length = min(get_robot_paths(seq, 2, direction_cache[0], direction_cache[1]) for seq in possible_sequences)
        numeric_part = int(code[:3])
        print(code, "-", min_length, "*", numeric_part)
        total_complexity += min_length * numeric_part
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
        possible_sequences = []
        for combination in product(*[get_sequence(numeric_cache[0], x, y) for x, y in zip("A" + code, code)]):
            possible_sequences.append("".join(combination))
        
        min_length = min(get_robot_paths(seq, 25, direction_cache[0], direction_cache[1]) for seq in possible_sequences)
        numeric_part = int(code[:3])
        print(code, "-", min_length, "*", numeric_part)
        total_complexity += min_length * numeric_part
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
