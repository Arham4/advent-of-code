#!/usr/bin/env python3

from pathlib import Path

import part1
import part2

def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        lines = f.read().splitlines()
        return lines

def main():
    example = read_file("example.txt")
    input = read_file("input.txt")

    print("--- Part One ---")
    part1.test(example)
    print("Result:", part1.result(input))

    print("--- Part Two ---")
    part2.test(example)
    print("Result:", part2.result(input))

if __name__ == "__main__":
    main()