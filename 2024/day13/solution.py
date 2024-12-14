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
import numpy
from fractions import Fraction
from math import gcd


def part1(inp):
    prizes_configs = []
    for i in range(0, len(inp), 4):
        button_a = inp[i].replace("Button A: ", "").replace("X+", "").replace("Y+", "")
        button_b = inp[i + 1].replace("Button B: ", "").replace("X+", "").replace("Y+", "")
        prize = inp[i + 2].replace("Prize: ", "").replace("X=", "").replace("Y=", "")
        
        a_offsets = [int(x) for x in button_a.split(", ")]
        b_offsets = [int(x) for x in button_b.split(", ")]
        prize_location = [int(x) for x in prize.split(", ")]

        prizes_configs.append(((a_offsets[0], a_offsets[1]), (b_offsets[0], b_offsets[1]), (prize_location[0], prize_location[1])))

    tokens = 0
    for (dx1, dy1), (dx2, dy2), (prize_x, prize_y) in prizes_configs:
        visited = set()
        queue = deque()
        queue.append((0, 0, 0))
        min_wins = float('inf')
        while queue:
            x, y, attempts = queue.popleft()
            if (x, y) in visited:
                continue
            if x > prize_x or y > prize_y:
                continue
            visited.add((x, y))
            if x == prize_x and y == prize_y:
                min_wins = min(min_wins, attempts)
                # print('won', prize_x, prize_y, "with", attempts, "tokens")
            else:
                queue.append((x + dx1, y + dy1, attempts + 3))
                queue.append((x + dx2, y + dy2, attempts + 1))
        if min_wins != float('inf'):
            tokens += min_wins
    return tokens


def solve_linear_system(a1, b1, c1, a2, b2, c2):
    A = numpy.array([[Fraction(a1), Fraction(b1)], 
                  [Fraction(a2), Fraction(b2)]])
    b = numpy.array([Fraction(c1), Fraction(c2)])
    
    det = A[0,0] * A[1,1] - A[0,1] * A[1,0]
    
    if det == 0:
        return None
    
    # Cramer's rule
    x = (b[0] * A[1,1] - b[1] * A[0,1]) / det
    y = (A[0,0] * b[1] - A[1,0] * b[0]) / det
    
    return x, y


def part2(inp):
    prizes_configs = []
    for i in range(0, len(inp), 4):
        button_a = inp[i].replace("Button A: ", "").replace("X+", "").replace("Y+", "")
        button_b = inp[i + 1].replace("Button B: ", "").replace("X+", "").replace("Y+", "")
        prize = inp[i + 2].replace("Prize: ", "").replace("X=", "").replace("Y=", "")
        
        a_offsets = [int(x) for x in button_a.split(", ")]
        b_offsets = [int(x) for x in button_b.split(", ")]
        prize_location = [int(x) + 10000000000000 for x in prize.split(", ")]

        prizes_configs.append(((a_offsets[0], a_offsets[1]), (b_offsets[0], b_offsets[1]), (prize_location[0], prize_location[1])))

    tokens = 0
    for (dx1, dy1), (dx2, dy2), (prize_x, prize_y) in prizes_configs:
        gcd_x = gcd(dx1, dx2)
        if prize_x % gcd_x != 0:
            continue
            
        gcd_y = gcd(dy1, dy2)
        if prize_y % gcd_y != 0:
            continue
        
        a, b = solve_linear_system(dx1, dx2, prize_x, dy1, dy2, prize_y)

        if a.denominator > 1 or b.denominator > 1:
            continue

        tokens += a * 3 + b
    return tokens


def p1_test(examples):
    example = 0
    exp = 480
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    '''
    example = 0
    exp = 0
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    '''
