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

A = 0
B = 1
C = 2

ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7


def execute_program(register, program):
    def find_combo_operand(pointer):
        combo_operand = program[pointer]
        return combo_operand if combo_operand <= 3 else register[A] if combo_operand == 4 else register[B] if combo_operand == 5 else register[C] if combo_operand == 6 else 'invalid'

    pointer = 0
    output = ""
    while pointer < len(program):
        opcode = program[pointer]
        if opcode == ADV:
            combo_operand = find_combo_operand(pointer + 1)
            if combo_operand != 'invalid':
                register[A] = int(register[A] // pow(2, combo_operand))
        elif opcode == BXL:
            literal_operand = program[pointer + 1]
            register[B] = register[B] ^ literal_operand
        elif opcode == BST:
            combo_operand = find_combo_operand(pointer + 1)
            register[B] = combo_operand % 8
        elif opcode == JNZ and register[A] != 0:
            literal_operand = program[pointer + 1]
            pointer = literal_operand
            continue
        elif opcode == BXC:
            register[B] = register[B] ^ register[C]
        elif opcode == OUT:
            combo_operand = find_combo_operand(pointer + 1)
            output += f',{combo_operand % 8}'
        elif opcode == BDV:
            combo_operand = find_combo_operand(pointer + 1)
            if combo_operand != 'invalid':
                register[B] = int(register[A] // pow(2, combo_operand))
        elif opcode == CDV:
            combo_operand = find_combo_operand(pointer + 1)
            if combo_operand != 'invalid':
                register[C] = int(register[A] // pow(2, combo_operand))
        pointer += 2
    return output[1:]


def part1(inp):
    register = [int(inp[i].split(": ")[1]) for i in range(3)]
    program = [int(x) for x in inp[4].split(": ")[1].split(",")]
    return execute_program(register, program)


def find_a_for_expected_value(a, expected_value):
    # done to get correct a and undo adv 3 instruction
    a = int(a * pow(2, 3))
    possible_a_values = []
    for possible_a in range(a, a + 8):
        '''
        # adv 3: a = a / 2^3
        my_a = int(possible_a / pow(2, 3))
        # out 4: out a % 8
        if my_a % 8 == expected_value:
            possible_a_values.append(possible_a)
        # jnz 0: jnz 0
        '''
        
        # TODO ideally use execute_program for this instead of having to do this manually

        # bst 4: b % 8
        b = possible_a % 8
        # bxl 5: b^5
        b ^= 5
        # cdv 5: c = a / 2^b
        c = int(possible_a / pow(2, b))
        # bxl 6: b^6
        b ^= 6
        # adv 3: a = a / 2^3
        # bxc 6: b = b^c
        b ^= c
        # out 5: out b % 8
        if b % 8 == expected_value:
            possible_a_values.append(possible_a)
        # jnz 0: jnz 0
        # 
        # while a:
        #   output (b^(a / 2^((b % 8)^5)) % 8
        #   a = a / 2^3
    return possible_a_values


def part2(inp):
    original_register = [int(inp[i].split(": ")[1]) for i in range(3)]
    original_program = inp[4].split(": ")[1].split(",")
    program = [int(x) for x in original_program]
    desired_result = ",".join(original_program)

    a_values = [0]
    for expected_value in reversed(program):
        attempt = []
        for a in a_values:
            attempt += find_a_for_expected_value(a, expected_value)
        a_values = attempt
    return min(a_values)


def p1_test(examples):
    example = 0
    exp = "4,6,3,5,6,3,5,2,1,0"
    res = part1(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"


def p2_test(examples):
    '''
    example = 0
    exp = 117440
    res = part2(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
    '''
