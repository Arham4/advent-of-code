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


def solution(inp):
    blocking_coords = set()
    for i in inp:
        line = i.split(' -> ')

        for j in range(1, len(line)):
            prev = line[j - 1].split(',')
            curr = line[j].split(',')

            if prev[0] == curr[0]:
                smaller = min(int(prev[1]), int(curr[1]))
                larger = max(int(prev[1]), int(curr[1]))
                for k in range(smaller, larger + 1):
                    blocking_coords.add((int(prev[0]), k))
            elif prev[1] == curr[1]:
                smaller = min(int(prev[0]), int(curr[0]))
                larger = max(int(prev[0]), int(curr[0]))
                for k in range(smaller, larger + 1):
                    blocking_coords.add((k, int(prev[1])))

    start = [500, 0]
    finished = 0
    while True:
        curr = start[:]
        prev = curr[:]

        while True:
            if (curr[0], curr[1] + 1) not in blocking_coords:
                curr[1] += 1
            elif (curr[0] - 1, curr[1] + 1) not in blocking_coords:
                curr[0] -= 1
                curr[1] += 1
            elif (curr[0] + 1, curr[1] + 1) not in blocking_coords:
                curr[0] += 1
                curr[1] += 1

            # Pretty broken solution btw goes on forever
            if prev == curr:
                blocking_coords.add((curr[0], curr[1]))
                finished += 1
                break

            prev = curr[:]

        if curr == start:
            break

    return finished




def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 24
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"