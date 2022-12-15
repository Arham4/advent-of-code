from typing import List, Tuple

import part1


def remove_overlaps(ranges: List[Tuple[int, int]]):
    for i in range(len(ranges) - 1):
        if ranges[i][1] + 1 >= ranges[i + 1][0]:
            ranges[i] = (min(ranges[i][0], ranges[i + 1][0]), max(ranges[i][1], ranges[i + 1][1]))
            ranges.pop(i + 1)
            remove_overlaps(ranges)
            break


def solution(inp: List[str], limit: int):
    sensors, distances, beacons = part1.parse_input(inp)

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


def result(inp: List[str], limit: int):
    return solution(inp, limit)


def test(examples: List[List[str]]):
    example = 0
    exp = 56000011
    res = result(examples[example], 20)
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
