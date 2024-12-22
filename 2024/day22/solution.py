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


def mix(secret_num, num):
    return secret_num ^ num


def prune(secret_num):
    return secret_num % 16777216


def calculate_next_secret_num(secret_num):
    secret_num = prune(mix(secret_num, secret_num * 64))
    secret_num = prune(mix(secret_num, secret_num // 32))
    secret_num = prune(mix(secret_num, secret_num * 2048))
    return secret_num


def get_price(secret_num):
    return secret_num % 10


def part1(inp):
    total = 0
    for line in inp:
        secret_num = int(line)
        for _ in range(2000):
            secret_num = calculate_next_secret_num(secret_num)
        total += secret_num
    return total


def part2(inp):
    bananas_overall = Counter()
    
    for line in inp:
        secret_num = int(line)
        latest_sequence = deque([None] * 4, maxlen=4)
        bananas = Counter()
        seen_sequences = set()
        
        prev_price = get_price(secret_num)
        
        for _ in range(2000):
            secret_num = calculate_next_secret_num(secret_num)
            new_price = get_price(secret_num)
            
            price_change = new_price - prev_price
            latest_sequence.append(price_change)
            
            sequence = tuple(latest_sequence)
            
            if None not in sequence and sequence not in seen_sequences:
                bananas[sequence] = new_price
                seen_sequences.add(sequence)
            
            prev_price = new_price
        
        bananas_overall.update(bananas)
    return bananas_overall.most_common(1)[0][1]


def p1_test(examples):
    example = 0
    exp = 37327623
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 23
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
