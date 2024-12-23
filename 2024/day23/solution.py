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


def parse_graph(inp):
    graph = {}
    for line in inp:
        a, b = line.split('-')
        if a not in graph: graph[a] = set()
        if b not in graph: graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph


def bron_kerbosch(graph, current_clique=None, candidates=None, exclusions=None, cliques=None):
    if current_clique is None: 
        current_clique = set()
    if candidates is None: 
        candidates = set(graph.keys())
    if exclusions is None: 
        exclusions = set()
    if cliques is None: 
        cliques = []
    
    if not candidates and not exclusions:
        cliques.append(current_clique)
        return
    
    max_intersection_size = -1
    pivot = None

    for node in candidates.union(exclusions):
        intersection_size = len(graph[node].intersection(candidates))
        if intersection_size > max_intersection_size:
            max_intersection_size = intersection_size
            pivot = node
    
    reduction = graph[pivot] if pivot else set()

    for v in candidates - reduction:
        neighbors = graph[v]
        bron_kerbosch(graph,
            current_clique.union({v}),
            candidates.intersection(neighbors),
            exclusions.intersection(neighbors),
            cliques)
        candidates.remove(v)
        exclusions.add(v)
    
    return cliques


def find_triplets(clique):
    return {tuple(sorted(triplet)) for triplet in combinations(clique, 3)}


def part1(inp):
    graph = parse_graph(inp)
    cliques = bron_kerbosch(graph)
    
    unique_triplets = set()
    for c in cliques:
        if len(c) >= 3:
            unique_triplets.update(find_triplets(c))
    return sum(1 for t in unique_triplets if any(n.startswith('t') for n in t))


def part2(inp):
    graph = parse_graph(inp)
    cliques = bron_kerbosch(graph)
    max_clique = max(cliques, key=len)
    return ','.join(sorted(max_clique))


def p1_test(examples):
    example = 0
    exp = 7
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    example = 0
    exp = "co,de,ka,ta"
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"