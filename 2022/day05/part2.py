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
    stacks = defaultdict(list)
    moving = False
    for line in inp:
        if line.startswith(' 1') or line == '':
            moving = True
            continue
        if not moving:
            for current_index in range(0, len(line), 4):
                letter = line[current_index:current_index + 4].strip()
                if letter != '':
                    current_group = (current_index // 4) + 1
                    stacks[current_group].insert(0, letter)
        else:
            split = line.split(' ')
            amount = int(split[1])
            from_group = int(split[3])
            to_group = int(split[5])

            to_move = []
            for i in range(amount):
                to_move.insert(0, stacks[from_group].pop())
            for move in to_move:
                stacks[to_group].append(move)
    output = ''
    for key in sorted(stacks.keys()):
        output += stacks[key][-1].replace('[', '').replace(']', '')
    return output

def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 'MCD'
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
