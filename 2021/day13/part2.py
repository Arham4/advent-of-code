import part1


def print_pretty(grid):
    for y in range(len(grid)):
        ignore = True
        for x in range(len(grid[y])):
            if grid[y][x] == '##':
                ignore = False
                break
        if not ignore:
            for x in range(len(grid[y])):
                print(grid[y][x], end='')
            print('\n')


def solution(inp):
    grid = part1.solution(inp, True)
    print_pretty(grid)


def result(inp):
    return solution(inp)
