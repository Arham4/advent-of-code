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


def perform_bfs(grid, width, height):
    visited = set()
    queue = deque([(0, 0, 0)])
    min_steps = float('inf')
    while queue:
        y, x, steps = queue.popleft()

        if (y, x) in visited:
            continue

        if y == height - 1 and x == width - 1:
            min_steps = min(min_steps, steps)
            continue

        visited.add((y, x))

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < height and 0 <= new_x < width:
                if grid[new_y][new_x] != '#':
                    queue.append((new_y, new_x, steps + 1))
                    
    return min_steps


def construct_grid(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]


def populate_bytes(inp, grid, bytes):
    for i in range(bytes):
        x, y = map(int, inp[i].split(','))
        grid[y][x] = '#'


def part1(inp, bytes=1024, width=71, height=71):
    grid = construct_grid(width, height)
    populate_bytes(inp, grid, bytes)
    return perform_bfs(grid, width, height)


def part2(inp, width=71, height=71):
    left = 0
    right = len(inp)
        
    previous = -1
    while left < right:
        mid = (left + right) // 2
        
        grid = construct_grid(width, height)
        populate_bytes(inp, grid, mid)
        min_steps = perform_bfs(grid, width, height)
        
        if min_steps != float('inf'):
            previous = mid
            left = mid + 1
        else:
            right = mid
    
    return inp[previous]


def p1_test(examples):
    example = 0
    exp = 22
    res = part1(examples[example], bytes=12, width=7, height=7)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = "6,1"
    res = part2(examples[example], width=7, height=7)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
