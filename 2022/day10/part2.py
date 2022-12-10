from typing import List


def light_pixel(grid: List[List[str]], cycles: int, x: int) -> None:
    p = cycles % len(grid[0])
    if x - 1 == p or x == p or x + 1 == p:
        y = cycles // len(grid[0])
        grid[y][p] = '#'


def solution(inp: List[str]) -> None:
    grid = []
    for i in range(6):
        grid.append(['.' for i in range(40)])

    x = 1
    cycles = 0
    for line in inp:
        if line == 'noop':
            light_pixel(grid, cycles, x)
            cycles += 1
        else:
            amount = int(line.split(' ')[1])
            for i in range(2):
                light_pixel(grid, cycles, x)
                cycles += 1

            x += amount

            light_pixel(grid, cycles, x)

    for row in grid:
        for column in row:
            print(column, end='')
        print()


def result(inp: List[str]) -> None:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    '''
    example = 0
    res = result(examples[example])
    '''
