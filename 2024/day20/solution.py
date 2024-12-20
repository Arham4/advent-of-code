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


def part1(inp, minimum=100):
    start = None
    end = None
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == 'S':
                start = (y, x)
            elif inp[y][x] == 'E':
                end = (y, x)
            if start and end:
                break
        if start and end:
            break

    start_times = {start: 0}
    end_times = {end: 0}
    queue = deque([(start, 0, start_times), (end, 0, end_times)])

    while queue:
        (y, x), picoseconds, picoseconds_to_node = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < len(inp) and 0 <= new_x < len(inp[0]):
                if inp[y + dy][x + dx] != '#':
                    new_pos = (new_y, new_x)
                    if new_pos not in picoseconds_to_node:
                        picoseconds_to_node[new_pos] = picoseconds + 1
                        queue.append((new_pos, picoseconds + 1, picoseconds_to_node))
    
    best_picoseconds = start_times[end]
    cheats_count = 0
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if (y, x) not in start_times:
                continue

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= y + dy < len(inp) and 0 <= x + dx < len(inp[0]):
                    for dy2, dx2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= y + dy + dy2 < len(inp) and 0 <= x + dx + dx2 < len(inp[0]):
                            if inp[y + dy + dy2][x + dx + dx2] != '#' and (y + dy + dy2, x + dx + dx2) in end_times:
                                time_to_end = start_times[(y, x)] + 2 + end_times[(y + dy + dy2, x + dx + dx2)]
                                if best_picoseconds - time_to_end >= minimum:
                                    cheats_count += 1
    return cheats_count


def part2(inp, minimum=100):
    start = None
    end = None
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == 'S':
                start = (y, x)
            elif inp[y][x] == 'E':
                end = (y, x)
            if start and end:
                break
        if start and end:
            break

    start_times = {start: 0}
    end_times = {end: 0}
    queue = deque([(start, 0, start_times), (end, 0, end_times)])

    while queue:
        (y, x), picoseconds, picoseconds_to_node = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y = y + dy
            new_x = x + dx
            if 0 <= new_y < len(inp) and 0 <= new_x < len(inp[0]):
                if inp[y + dy][x + dx] != '#':
                    new_pos = (new_y, new_x)
                    if new_pos not in picoseconds_to_node:
                        picoseconds_to_node[new_pos] = picoseconds + 1
                        queue.append((new_pos, picoseconds + 1, picoseconds_to_node))
    
    best_picoseconds = start_times[end]
    valid_cheats = set()

    cheat_vectors = [(dy, dx) for dy in range(-20, 21) for dx in range(-20, 21) if abs(dy) + abs(dx) <= 20]

    for (y, x) in start_times.keys():
        if (y, x) not in start_times:
            continue

        time_till = start_times[(y, x)]
        if time_till >= best_picoseconds:
            continue

        for dy, dx in cheat_vectors:
            new_y = y + dy
            new_x = x + dx
            new_pos = (new_y, new_x)

            if 0 <= new_y < len(inp) and 0 <= new_x < len(inp[0]):
                if inp[new_y][new_x] != '#' and new_pos in end_times:
                    cheat_length = abs(dy) + abs(dx)
                    new_time = time_till + cheat_length + end_times[new_pos]

                    if best_picoseconds - new_time >= minimum:
                        valid_cheats.add(((y, x), new_pos))

    return len(valid_cheats)


def p1_test(examples):
    example = 0
    exp = 44
    res = part1(examples[example], minimum=2)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 285
    res = part2(examples[example], minimum=50)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
