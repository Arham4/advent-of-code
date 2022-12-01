#!/usr/bin/env python3

from pathlib import Path
import os

import part1
import part2


def read_file(filename, split_lines):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        file = f.read()
        if split_lines:
            return file.splitlines()
        return file


def main():
    split_lines = True
    examples = [read_file(f, split_lines) for f in os.listdir('.') if os.path.isfile(f) and f.startswith("example")]
    input = read_file("input.txt", split_lines)

    print("--- Part One ---")
    part1.test(examples)
    print("Result:", part1.result(input))

    print("--- Part Two ---")
    part2.test(examples)
    print("Result:", part2.result(input))


if __name__ == "__main__":
    main()
