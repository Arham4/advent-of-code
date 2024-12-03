import os
import requests
import pathlib
import json
import part1
import part2


def read_file(filename: str, split_lines: bool):
    path = pathlib.Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        file = f.read()
        if split_lines:
            return file.splitlines()
        return file


def save_file(filename: str, text: str) -> None:
    with open(filename, 'w+') as file:
        file.write(text)


def read_input(split_lines: bool):
    day = pathlib.PurePath(__file__).parent.name.replace('day0', '').replace('day', '')

    with open('../cookies.json', 'r') as cookies_file:
        cookies = json.load(cookies_file)
        input_url = 'https://adventofcode.com/2024/day/' + day + '/input'
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

    p1_examples = [read_file(f, split_lines) for f in os.listdir('.') if os.path.isfile(f) and f.startswith("p1_example")]
    p2_examples = [read_file(f, split_lines) for f in os.listdir('.') if os.path.isfile(f) and f.startswith("p2_example")]
    input = read_input(split_lines)
    output = open("output.txt", "w+")

    print("--- Part One ---")
    if p1_examples[0]:
        part1.test(p1_examples)
        print("Test passed")
    result = part1.result(input)
    print("Result:", result)

    if p2_examples[0]:
        print("--- Part Two ---")
        part2.test(p2_examples)
        print("Test passed")
        result2 = part2.result(input)
        if result2:
            output.write(str(result2))
        else:
            output.write(str(result))
        output.close()
    
        print("Result:", result2)
    else:
        output.write(str(result))
        output.close()


if __name__ == "__main__":
    main()
