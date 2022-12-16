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


def find_best_choice(current, destinations, best_choice):
    to = destinations[current]
    best = min(to, key=lambda x: shortest_path_to(x, destinations, best_choice))
    return best


def find_best_choice_2(current, destinations, pressures, opened, minutes_remaining):
    values = []
    print('from', current)
    for pressure in pressures.keys():
        distance = shortest_path_to(current, destinations, pressure)
        values.append((pressure, (minutes_remaining - distance - 1) * pressures[pressure]))
    print(values)

    '''pressures_sorted = sorted(pressures.keys(), key=lambda x: shortest_path_to(current, destinations, x))
    pressures_sorted = sorted(pressures_sorted, key=lambda x: pressures[x] - shortest_path_to(current, destinations, x), reverse=True)
    pressures_sorted = [x for x in pressures_sorted if x not in opened]
    # print('from', current, '', end = '')
    for pressure in pressures_sorted:
        dist = shortest_path_to(current, destinations, pressure)
    #     print(pressure, dist, pressures[pressure] - dist, '', end='')
    # print()
    return pressures_sorted[0]
    '''


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

    pressure = 0
    queue = ['AA']
    # choices = set()
    opened = set()
    sum = 0

    minutes_remaining = 31
    while minutes_remaining >= 0:
        minutes_remaining -= 1
        sum += pressure
        print(sum, pressure, minutes_remaining)

        if len(queue) == 0:
            continue

        current_location = queue.pop()

        '''
        print('new best choice', find_best_choice_2(current_location, destinations, flow_rates, opened))

        choices.update([x for x in destinations[current_location] if x not in opened])
        if current_location not in opened:
            choices.add(current_location)

        if len(choices) == 0:
            continue

        best_choice = max(choices, key=lambda x: flow_rates[x])
        '''
        best_choice = find_best_choice_2(current_location, destinations, flow_rates, opened, minutes_remaining)
        if best_choice == current_location or flow_rates[best_choice] == flow_rates[current_location] and current_location not in opened:
            minutes_remaining -= 1

            pressure += flow_rates[current_location]
            opened.add(current_location)

            # choices.remove(best_choice)

            # if len(choices) == 0:
            #     continue

            best_choice = find_best_choice_2(current_location, destinations, flow_rates, opened, minutes_remaining)

        queue.append(find_best_choice(current_location, destinations, best_choice))
        print(current_location, best_choice, queue)

    return sum
def result(inp):
    return solution(inp)


def test(examples):
    example = 0
    exp = 1651
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
