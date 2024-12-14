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


def part1(inp, width=101, height=103):
    quadrants = defaultdict(list)
    middle_width = width // 2
    middle_height = height // 2
    for line in inp:
        split = line.split(" ")
        position = [int(x) for x in split[0].replace("p=", "").split(",")]
        velocity = [int(x) for x in split[1].replace("v=", "").split(",")]
        position[0] = (position[0] + velocity[0] * 100) % width
        position[1] = (position[1] + velocity[1] * 100) % height

        if position[0] != middle_width and position[1] != middle_height:
            if position[0] < middle_width and position[1] < middle_height:
                quadrants["nw"].append(position)
            elif position[0] < middle_width and position[1] > middle_height:
                quadrants["ne"].append(position)
            elif position[0] > middle_width and position[1] < middle_height:
                quadrants["sw"].append(position)
            elif position[0] > middle_width and position[1] > middle_height:
                quadrants["se"].append(position)
    summation = 1
    for name, quadrant in quadrants.items():
        summation *= len(quadrant)
    return summation


def part2(inp, width=101, height=103):
    output = open('output_real.txt', 'w+')
    for i in range(1, 10000):
        positions = []
        middle_width = width // 2
        middle_height = height // 2
        for line in inp:
            split = line.split(" ")
            position = [int(x) for x in split[0].replace("p=", "").split(",")]
            velocity = [int(x) for x in split[1].replace("v=", "").split(",")]
            position[0] = (position[0] + velocity[0] * i) % width
            position[1] = (position[1] + velocity[1] * i) % height

            positions.append(position)

        grid = [['.'] * width for _ in range(height)]
        for x, y in positions:
            grid[y][x] = '#'
        output.write('After ' + str(i) + ' seconds')
        output.write("\n")
        output.write('\n'.join(''.join(row) for row in grid))
        output.write("\n")
    output.close()
    # Then just look at output_real.txt to find the christmas tree
    return None


def p1_test(examples):
    example = 0
    exp = 12
    res = part1(examples[example], width=11, height=7)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    '''
    example = 0
    exp = 10
    res = part2(examples[example], width=11, height=7)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    '''