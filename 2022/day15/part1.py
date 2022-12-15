import collections
import sys
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


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


'''
My original flood-fill solution before I realized the problem needs to be more optimized lol

def fill_manhattan(x, y, distance, locations, sensors, beacons, visited):
    if distance == -1:
        return

    if (x, y) not in sensors and (x, y) not in beacons:
        locations[y].add(x)

    visited.add((x, y))

    fill_manhattan(x + 1, y, distance - 1, locations, sensors, beacons, visited)
    fill_manhattan(x - 1, y, distance - 1, locations, sensors, beacons, visited)
    fill_manhattan(x, y + 1, distance - 1, locations, sensors, beacons, visited)
    fill_manhattan(x, y - 1, distance - 1, locations, sensors, beacons, visited)
'''


def solution(inp, target):
    sensors = set()
    distances = {}
    beacons = set()
    locations = defaultdict(set)
    for line in inp:
        split = line.split(': ')
        sensor_x = int(split[0][split[0].index('x=') + 2:split[0].index(', ')])
        sensor_y = int(split[0][split[0].index('y=') + 2:])
        beacon_x = int(split[1][split[1].index('x=') + 2:split[1].index(', ')])
        beacon_y = int(split[1][split[1].index('y=') + 2:])

        distance = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        distances[(sensor_x, sensor_y)] = distance

        sensors.add((sensor_x, sensor_y))
        beacons.add((beacon_x, beacon_y))

    for sensor in sensors:
        distance = distances[sensor]
        distance_to = distance - abs(sensor[1] - target)

        if distance_to <= 0:
            continue

        locations_at = [sensor[0] + 1 + i for i in range(distance_to) if (sensor[0] + 1 + i, target) not in beacons] \
                       + [sensor[0] - 1 - i for i in range(distance_to) if (sensor[0] - 1 - i, target) not in beacons] \
                       + [sensor[0]]
        locations[target].update(locations_at)

        # fill_manhattan(sensor[0], sensor[1], distance, locations, sensors, beacons)

    return len(locations[target])


def result(inp, target):
    return solution(inp, target)


def test(examples):
    example = 0
    exp = 26
    res = result(examples[example], 10)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
