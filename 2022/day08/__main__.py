from typing import List, Tuple
import os
import requests
import pathlib
import json
import part1
import part2


def read_file(filename: str, split_lines: bool) -> str:
    path = pathlib.Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        file = f.read()
        if split_lines:
            return file.splitlines()
        return file


def save_file(filename: str, text: str):
    with open(filename, 'w+') as file:
        file.write(text)


def read_input(split_lines: bool) -> str:
    day = pathlib.PurePath(__file__).parent.name.replace('day0', '').replace('day', '')

    with open('../cookies.json', 'r') as cookies_file:
        cookies = json.load(cookies_file)
        input_url = 'https://adventofcode.com/2022/day/' + day + '/input'
        response = requests.get(input_url, cookies=cookies, headers={'User-Agent': 'Mozilla/5.0'})

    if response.ok:
        text = response.text
        save_file('input.txt', text)
        if split_lines:
            return text.splitlines()
        return text
    else:
        return read_file('input.txt', split_lines)


def main() -> None:
    split_lines = True

    examples = [read_file(f, split_lines) for f in os.listdir('.') if os.path.isfile(f) and f.startswith("example")]
    input = read_input(split_lines)

    print("--- Part One ---")
    part1.test(examples)
    print("Result:", part1.result(input))

    print("--- Part Two ---")
    part2.test(examples)
    print("Result:", part2.result(input))


if __name__ == "__main__":
    main()
