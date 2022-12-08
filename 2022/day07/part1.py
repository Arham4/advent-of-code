from collections import defaultdict
from typing import List


def go_up_one_level(current_directory: str) -> str:
    if current_directory == '/':
        return '/'
    return current_directory[:current_directory.rfind('/')]


def find_size_of_directory(paths: dict, current_directory: str) -> int:
    amount = 0
    for file in paths[current_directory]:
        if file.startswith('dir '):
            name = file.replace('dir ', '')
            amount += find_size_of_directory(paths, current_directory + '/' + name)
        else:
            amount += int(file.split(' ')[0])
    return amount


def populate_paths(inp: List[str]) -> dict:
    paths = defaultdict(list)
    current_directory = ''
    populating = False
    for line in inp:
        if line.startswith('$ '):
            command = line.replace('$ ', '')
            if command.startswith('cd'):
                location = command.replace('cd ', '')
                populating = False
                if location == '/':
                    current_directory = '/'
                elif location == '..':
                    current_directory = go_up_one_level(current_directory)
                else:
                    current_directory += '/' + location
            elif command.startswith('ls'):
                populating = True
        elif populating:
            paths[current_directory].append(line)
    return paths


def solution(inp: List[str]) -> int:
    paths = populate_paths(inp)
    answer = 0
    limit = 100000
    for path in paths:
        size = find_size_of_directory(paths, path)
        if size <= limit:
            answer += size
    return answer


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 95437
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
