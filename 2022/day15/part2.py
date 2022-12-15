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
import part1


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def remove_overlaps(ranges):
    for i in range(len(ranges) - 1):
        if ranges[i][1] + 1 >= ranges[i + 1][0]:
            ranges[i] = (min(ranges[i][0], ranges[i + 1][0]), max(ranges[i][1], ranges[i + 1][1]))
            ranges.pop(i + 1)
            remove_overlaps(ranges)
            break


def solution(inp, limit):
    sensors = set()
    distances = {}
    beacons = set()

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

    for row in range(limit):
        ranges = []
        for sensor in sensors:
            distance = distances[sensor]
            distance_to = distance - abs(sensor[1] - row)

            if distance_to <= 0:
                continue

            ranges.append((max(0, sensor[0] - distance_to), min(sensor[0] + distance_to, limit)))

        ranges.sort()
        remove_overlaps(ranges)

        if len(ranges) == 2:
            y = row
            x = ranges[0][1] + 1
            return x * 4000000 + y

    return -1


def result(inp, limit):
    return solution(inp, limit)


def test(examples):
    example = 0
    exp = 56000011
    res = result(examples[example], 20)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
