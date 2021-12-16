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
    example4 = read_file("example4.txt")
    example5 = read_file("example5.txt")
    example6 = read_file("example6.txt")
    example7 = read_file("example7.txt")
    example8 = read_file("example8.txt")
    example9 = read_file("example9.txt")
    example10 = read_file("example10.txt")
    example11 = read_file("example11.txt")
    example12 = read_file("example12.txt")
    example13 = read_file("example13.txt")
    example14 = read_file("example14.txt")
    example15 = read_file("example15.txt")
    inp = read_file("input.txt")

    print("--- Part One ---")
    part1.test(example1, example2, example3, example4, example5, example6, example7)
    print("Result:", part1.result(inp))

    print("--- Part Two ---")
    part2.test(example8, example9, example10, example11, example12, example13, example14, example15)
    print("Result:", part2.result(inp))


if __name__ == "__main__":
    main()
