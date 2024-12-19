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


def part1(inp):
    phrases = inp[0].split(", ")
    words = inp[2:]
    completed = set()
    
    for word in words:
        queue = deque([word])
        visited = set()
        
        while queue:
            word_so_far = queue.pop()
            
            if word_so_far == "":
                completed.add(word)
                break
                
            key = word_so_far
            if key in visited:
                continue
            visited.add(key)
            
            for phrase in phrases:
                if word_so_far.startswith(phrase):
                    after = word_so_far[len(phrase):]
                    queue.append(after)
    
    return len(completed)


def part2(inp):
    phrases = tuple(sorted(inp[0].split(", ")))
    words = inp[2:]
    result = 0
    
    def find_combinations(remaining, cache):
        if remaining in cache:
            return cache[remaining]
            
        if not remaining:
            return 1
            
        total = 0
        for phrase in phrases:
            if remaining.startswith(phrase):
                total += find_combinations(remaining[len(phrase):], cache)
        
        cache[remaining] = total
        return total
    
    for word in words:
        cache = {}
        combinations = find_combinations(word, cache)
        result += combinations
        
    return result


def p1_test(examples):
    example = 0
    exp = 6
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = 16
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
