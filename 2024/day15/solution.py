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


def move(inp, position, y_step, x_step):
    y, x = position
    # print(inp[y][x], inp[y + y_step][x + x_step], y, x)
    if inp[y + y_step][x + x_step] == '.':
        inp[y][x] = '.'
        position = (y + y_step, x + x_step)
        inp[y + y_step][x + x_step] = '@'
        return position
    elif inp[y + y_step][x + x_step] == '#':
        return position
    elif inp[y + y_step][x + x_step] == 'O':
        extreme_y = y + y_step
        extreme_x = x + x_step

        if y_step != 0:
            for y_other in range(y + y_step, len(inp) if y_step > 0 else 0, y_step):
                if inp[y_other][x] == 'O':
                    extreme_y = y_other
                else:
                    break
        if x_step != 0:
            for x_other in range(x + x_step, len(inp[0]) if x_step > 0 else 0, x_step):
                if inp[y][x_other] == 'O':
                    extreme_x = x_other
                else:
                    break
        after_extreme = (extreme_y + y_step, extreme_x + x_step)
        if inp[after_extreme[0]][after_extreme[1]] == '#':
            return position
        # print(after_extreme[0], y if y_step != 0 else y + 1, y_step if y_step != 0 else 1)
        # print(after_extreme[1], x if x_step != 0 else x + 1, x_step if x_step != 0 else 1)

        for new_y in range(after_extreme[0], y - y_step if y_step != 0 else y + 1, -y_step if y_step != 0 else 1):
            for new_x in range(after_extreme[1], x - x_step if x_step != 0 else x + 1, -x_step if x_step != 0 else 1):
                if new_y == y + y_step and new_x == x + x_step:
                    # print("re-assign self")
                    inp[new_y][new_x] = '@'
                    position = (new_y, new_x)
                elif new_y == y and new_x == x:
                    # print("free old space")
                    inp[new_y][new_x] = '.'
                else:
                    # print('move box')
                    inp[new_y][new_x] = 'O'
        return position
    elif inp[y + y_step][x + x_step] in ['[', ']']:
        relevant_positions = set()

        def scan_relevant_positions(ry, rx):
            relevant_positions.add((ry, rx))
            # print('new add', (ry, rx))
            if inp[ry][rx] == '[':
                relevant_positions.add((ry, rx + 1))
                # print('add', (ry, rx + 1))
                if y_step != 0 and inp[ry + y_step][rx + 1] in ['[', ']', '#']:
                    scan_relevant_positions(ry + y_step, rx + 1)
            elif inp[ry][rx] == ']':
                relevant_positions.add((ry, rx - 1))
                # print('add', (ry, rx - 1))
                if y_step != 0 != ry and inp[ry + y_step][rx - 1] in ['[', ']', '#']:
                    scan_relevant_positions(ry + y_step, rx - 1)
            elif inp[ry][rx] == '#':
                relevant_positions.add("FAULTY")
                return
            if inp[ry + y_step][rx + x_step] in ['[', ']', '#']:
                scan_relevant_positions(ry + y_step, rx + x_step)

        scan_relevant_positions(y + y_step, x + x_step)

        if "FAULTY" in relevant_positions:
            return position

        relevant_positions = sorted(relevant_positions, reverse=False if y_step < 0 or x_step < 0 else True)
        # print('relevant positions', relevant_positions, y, x, y_step, x_step)
        for box_y, box_x in relevant_positions:
            inp[box_y + y_step][box_x + x_step], inp[box_y][box_x] = inp[box_y][box_x], inp[box_y + y_step][box_x + x_step]
        inp[y + y_step][x + x_step], inp[y][x] = inp[y][x], inp[y + y_step][x + x_step]
        return (y + y_step, x + x_step)
    return None


def part1(inp):
    inp = [list(inp[y]) for y in range(len(inp))]

    position = None
    find_initial = True
    instructions_index = None
    for y in range(len(inp)):
        if inp[y] == []:
            find_initial = False
            instructions_index = y + 1
            break
        for x in range(len(inp[y])):
            if find_initial and inp[y][x] == '@':
                position = (y, x)
                break
            
        if find_initial and position:
            continue
    
    for y in range(instructions_index, len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '<':
                position = move(inp, position, 0, -1)
            elif inp[y][x] == '>':
                position = move(inp, position, 0, 1)
            elif inp[y][x] == '^':
                position = move(inp, position, -1, 0)
            elif inp[y][x] == 'v':
                position = move(inp, position, 1, 0)
            '''
            print('Move', inp[y][x])
            for line in inp:
                if line == []:
                    break
                for x in line:
                    print(x, end="")
                print()
            print()
            '''
    
    summation = 0
    for y in range(instructions_index - 1):
        for x in range(len(inp[y])):
            if inp[y][x] == 'O':
                summation += 100 * y + x
    return summation


def part2(inp_raw):
    inp = []

    position = None
    find_initial = True
    instructions_index = None
    for y in range(len(inp_raw)):
        if inp_raw[y] == '':
            find_initial = False
            instructions_index = y + 1
            break
        inp.append([])
        for x in range(len(inp_raw[y])):
            if inp_raw[y][x] == '@':
                position = (y, len(inp[y]))
                inp[y].append(inp_raw[y][x])
                inp[y].append('.')
            elif inp_raw[y][x] == 'O':
                inp[y].append('[')
                inp[y].append(']')
            else:
                inp[y].append(inp_raw[y][x])
                inp[y].append(inp_raw[y][x])

    '''
    print('Initial state:')
    for line in inp:
        if line == []:
            break
        for x in line:
            print(x, end="")
        print()
    print()
    '''

    for y in range(instructions_index, len(inp_raw)):
        for x in range(len(inp_raw[y])):
            if inp_raw[y][x] == '<':
                position = move(inp, position, 0, -1)
            elif inp_raw[y][x] == '>':
                position = move(inp, position, 0, 1)
            elif inp_raw[y][x] == '^':
                position = move(inp, position, -1, 0)
            elif inp_raw[y][x] == 'v':
                position = move(inp, position, 1, 0)
            '''
            print('Move', inp_raw[y][x])
            for line in inp:
                if line == []:
                    break
                for x in line:
                    print(x, end="")
                print()
            print()
            '''
    
    summation = 0
    for y in range(instructions_index - 1):
        for x in range(len(inp[y])):
            if inp[y][x] == '[':
                summation += 100 * y + x
    return summation


def p1_test(examples):
    example = 0
    exp = 2028
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 10092
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 1
    exp = 618
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 0
    exp = 9021
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
