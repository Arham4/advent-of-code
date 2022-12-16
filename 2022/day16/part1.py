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


def shortest_path_to(start, destinations, end):
    visited = set()
    queue = [(start, 0)]
    while len(queue) > 0:
        current, distance = queue.pop(0)
        if current == end:
            return distance
        visited.add(current)
        for destination in destinations[current]:
            if destination not in visited:
                queue.append((destination, distance + 1))
    return math.inf


def potential(item):
    current, minutes, pressure, total_pressure, opened = item
    return total_pressure + pressure * (30 - minutes)


def solution(inp):
    flow_rates = {}
    destinations = {}

    for line in inp:
        split = line.split('; ')
        valve = split[0].split('has flow rate=')[0].replace('Valve ', '').strip()
        flow_rate = int(split[0].split('has flow rate=')[1].strip())
        lead_to = split[1].replace('valves', 'valve').replace('leads', 'lead').replace('tunnels', 'tunnel').replace('tunnel lead to valve ', '').strip().split(', ')

        flow_rates[valve] = flow_rate
        destinations[valve] = lead_to

    valves = list(flow_rates.keys())

    distances = {}
    for valve in valves:
        for other in valves:
            distances[(valve, other)] = shortest_path_to(valve, destinations, other)

    valves = [x for x in valves if flow_rates[x] > 0]

    max_pressure = 0
    queue = [('AA', 0, 0, 0, valves)]
    while len(queue) != 0:
        item = queue.pop()
        current, minutes, pressure, total_pressure, remaining = item

        max_pressure = max(max_pressure, potential(item))

        for valve in remaining:
            distance = distances[(current, valve)]
            if minutes + 1 + distance <= 30:
                queue.append((valve, minutes + 1 + distance, pressure + flow_rates[valve], total_pressure + pressure * (distance + 1), [x for x in remaining if x != valve]))

    return max_pressure


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 1651
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    print('passed')
