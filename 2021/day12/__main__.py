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
    example1 = read_file("example1.txt")
    example2 = read_file("example2.txt")
    example3 = read_file("example3.txt")
    inp = read_file("input.txt")

    print("--- Part One ---")
    part1.test(example1, example2, example3)
    print("Result:", part1.result(inp))

    print("--- Part Two ---")
    part2.test(example1)
    print("Result:", part2.result(inp))


if __name__ == "__main__":
    main()
