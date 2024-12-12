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


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def create_stone_linked_list(inp):
    stones_raw = inp[0].split(" ")

    current_stone = Node(stones_raw[0])
    head = current_stone
    previous_stone = None
    for i in range(1, len(stones_raw)):
        stone_raw = stones_raw[i]
        current_stone.next = Node(stone_raw)
        current_stone.prev = previous_stone
        previous_stone = current_stone
        current_stone = current_stone.next
    current_stone.prev = previous_stone

    return head


def blink(head):
    current_stone = head
    while current_stone:
        # print(current_stone.value, len(current_stone.value), current_stone.next, current_stone.prev, current_stone)
        if current_stone.value == "0":
            current_stone.value = str(1)
            current_stone = current_stone.next
        elif len(current_stone.value) % 2 != 0:
            current_stone.value = str(int(current_stone.value) * 2024)
            current_stone = current_stone.next
        elif len(current_stone.value) % 2 == 0:
            mid = len(current_stone.value) // 2
            left_stone = str(int(current_stone.value[:mid]))
            right_stone = str(int(current_stone.value[mid:]))

            current_left = current_stone.prev
            current_right = current_stone.next

            new_left = Node(left_stone)
            new_right = Node(right_stone)
            new_left.next = new_right
            new_right.prev = new_left

            if current_left:
                current_left.next = new_left
                new_left.prev = current_left
            if current_right:
                current_right.prev = new_right
                new_right.next = current_right

            if current_stone == head:
                head = new_left

            current_stone = current_right
    #print("\nAfter", str(i + 1), "blink:")
    return head

def blink_multiple_times(head, blinks):
    for i in range(blinks):
        head = blink(head)
    return head


def count_stones(head):
    current_stone = head
    count = 0
    while current_stone:
        current_stone = current_stone.next
        count += 1
    return count


def part1(inp):
    head = create_stone_linked_list(inp)
    head = blink_multiple_times(head, 25)
    return count_stones(head)


def part2(inp):
    head = create_stone_linked_list(inp)
    head = blink_multiple_times(head, 75)
    return count_stones(head)


def p1_test(examples):
    example = 0
    exp = 55312
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    '''
    example = 0
    exp = 0
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    '''
