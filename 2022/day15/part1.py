from typing import List
from collections import *


def manhattan_distance(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)


def parse_input(inp: List[str]):
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

    return sensors, distances, beacons


def solution(inp: List[str], target: int):
    locations = defaultdict(set)
    sensors, distances, beacons = parse_input(inp)

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


'''
My original flood-fill solution before I realized the problem needs to be more optimized lol

def fill_manhattan(x, y, distance, locations, sensors, beacons):
    if distance == -1:
        return

    if (x, y) not in sensors and (x, y) not in beacons:
        locations[y].add(x)

    fill_manhattan(x + 1, y, distance - 1, locations, sensors, beacons)
    fill_manhattan(x - 1, y, distance - 1, locations, sensors, beacons)
    fill_manhattan(x, y + 1, distance - 1, locations, sensors, beacons)
    fill_manhattan(x, y - 1, distance - 1, locations, sensors, beacons)
'''


def result(inp: List[str], target: int):
    return solution(inp, target)


def test(examples: List[List[str]]):
    example = 0
    exp = 26
    res = result(examples[example], 10)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
