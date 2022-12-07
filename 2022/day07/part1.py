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


def go_up_one_level(current_directory):
    if current_directory == '/':
        return '/'
    return current_directory[:current_directory.rfind('/')]


def find_size_of_directory(paths, current_directory):
    amount = 0
    for file in paths[current_directory]:
        if file.startswith('dir '):
            name = file.replace('dir ', '')
            amount += find_size_of_directory(paths, current_directory + '/' + name)
        else:
            amount += int(file.split(' ')[0])
    return amount


def populate_paths(inp):
    paths = defaultdict(list)
    current_directory = ''
    populating = False
    for line in inp:
        if line.startswith('$ '):
            command = line.replace('$ ', '')
            if command.startswith('cd'):
                location = command.replace('cd ', '')
                populating = False
                if location == '/':
                    current_directory = '/'
                elif location == '..':
                    current_directory = go_up_one_level(current_directory)
                else:
                    current_directory += '/' + location
            elif command.startswith('ls'):
                populating = True
        elif populating:
            paths[current_directory].append(line)
    return paths


def solution(inp):
    paths = populate_paths(inp)
    answer = 0
    limit = 100000
    for path in paths:
        size = find_size_of_directory(paths, path)
        if size <= limit:
            answer += size
    return answer


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 95437
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
