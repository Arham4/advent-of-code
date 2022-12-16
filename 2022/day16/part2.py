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
import part1_old


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
    currents, minutes, pressures, total_pressures, opened, you_path, elephant_path = item

    you_potential = total_pressures[0] + pressures[0] * (26 - minutes[0])
    elephant_potential = total_pressures[1] + pressures[1] * (26 - minutes[1])
    return you_potential + elephant_potential


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
    queue = [(('AA', 'AA'), (0, 0), (0, 0), (0, 0), valves, [], [])]
    while len(queue) != 0:
        item = queue.pop()
        currents, minutes, pressures, total_pressures, remaining, you_path, elephant_path = item
        you_path = you_path[:]
        elephant_path = elephant_path[:]

        you_path.append(currents[0])
        elephant_path.append(currents[1])

        max_pressure = max(max_pressure, potential(item))

        for valve in remaining:
            you_distance = distances[(currents[0], valve)]
            elephant_distance = distances[(currents[1], valve)]

            you_can_go = minutes[0] + 1 + you_distance <= 26
            elephant_can_go = minutes[1] + 1 + elephant_distance <= 26

            you_pressure = flow_rates[valve] * (26 - minutes[0] - you_distance - 1)
            elephant_pressure = flow_rates[valve] * (26 - minutes[1] - elephant_distance - 1)

            if max(you_pressure, elephant_pressure) <= 0:
                continue

            if you_pressure >= elephant_pressure and you_can_go:
                queue.append(((valve, currents[1]), (minutes[0] + 1 + you_distance, minutes[1]), (pressures[0] + flow_rates[valve], pressures[1]), (total_pressures[0] + pressures[0] * (you_distance + 1), total_pressures[1]), [x for x in remaining if x != valve], you_path, elephant_path))
            elif elephant_can_go:
                queue.append(((currents[0], valve), (minutes[0], minutes[1] + 1 + elephant_distance), (pressures[0], pressures[1] + flow_rates[valve]), (total_pressures[0], total_pressures[1] + pressures[1] * (elephant_distance + 1)), [x for x in remaining if x != valve], you_path, elephant_path))

    return max_pressure


def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 1707
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    print('passed')