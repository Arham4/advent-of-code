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
import time
from typing import *
from segment_tree import SegmentTree


def parse_disk_map(disk_map: str) -> List[Union[int, str]]:
    blocks = []
    file_id = 0
    for i in range(0, len(disk_map), 2):
        file_size = int(disk_map[i])
        blocks.extend([file_id] * file_size)

        if i + 1 < len(disk_map):
            free_size = int(disk_map[i + 1])
            blocks.extend(['.'] * free_size)
        file_id += 1
    return blocks


def fragment_disk_by_block(blocks: List[Union[int, str]]) -> None:
    left = 0
    right = len(blocks) - 1
    while left < right:
        if blocks[right] == '.':
            right -= 1
            continue
        if blocks[left] != '.':
            left += 1
            continue
        blocks[left], blocks[right] = blocks[right], blocks[left]
        left += 1
        right -= 1


def fragment_disk_by_file(blocks: List[Union[int, str]]) -> None:
    tree = SegmentTree(0, len(blocks) - 1)
    for i, block in enumerate(blocks):
        if block == '.':
            tree.free(i)
    
    file_positions = defaultdict(list)
    for i, block in enumerate(blocks):
        if block != '.':
            file_positions[block].append(i)
    
    for file_id in sorted(file_positions.keys(), reverse=True):
        positions = file_positions[file_id]
        required_size = len(positions)
        target = tree.find_for_size(required_size)
        # print("target for", file_id, "was determined as", target)
        if target is not None and target < min(positions):
            for position in positions:
                blocks[position] = '.'
                tree.free(position)
            for i in range(required_size):
                blocks[target + i] = file_id
                tree.occupy(target + i)


def calculate_checksum(blocks: List[Union[int, str]]):
    return sum(i * block for i, block in enumerate(blocks) if block != '.')


def part1(inp):
    blocks = parse_disk_map(inp[0])
    fragment_disk_by_block(blocks)
    return calculate_checksum(blocks)


def part2(inp):
    blocks = parse_disk_map(inp[0])
    fragment_disk_by_file(blocks)
    return calculate_checksum(blocks)


def p1_test(examples):
    example = 0
    exp = 60
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 1
    exp = 1928
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"

    example = 2
    exp = 10
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 2858
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
