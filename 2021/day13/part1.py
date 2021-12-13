import part2


def solution(inp, all_instructions):
    grid = {}
    index = 0
    largest_x = 0
    largest_y = 0

    for i in range(len(inp)):
        line = inp[i]
        if line == '':
            index += 1
            break
        coords = line.split(',')
        y = int(coords[1])
        x = int(coords[0])
        if y not in grid:
            grid[y] = {}
        grid[y][x] = '##'

        if y > largest_y:
            largest_y = y
        if x > largest_x:
            largest_x = x

        index += 1

    for x in range(largest_x + 1):
        for y in range(largest_y + 1):
            if y not in grid:
                grid[y] = {}
            if x not in grid[y]:
                grid[y][x] = '  '

    for i in range(index, len(inp)):
        line = inp[i]
        if 'x=' in line:
            fold = int(line.replace('fold along x=', ''))
            for y in grid:
                for x in range(fold + 1, len(grid[y])):
                    if grid[y][x] == '##':
                        offset = x - fold
                        grid[y][fold - offset] = grid[y][x]
                    grid[y][x] = '  '
        elif 'y=' in line:
            fold = int(line.replace('fold along y=', ''))
            for y in range(fold + 1, len(grid)):
                for x in grid[y]:
                    if grid[y][x] == '##':
                        offset = y - fold
                        grid[fold - offset][x] = '##'
                    grid[y][x] = '  '
        if not all_instructions:
            break
    return grid


def count_dots(grid):
    count = 0
    for y in grid:
        for x in grid[y]:
            if grid[y][x] == '##':
                count += 1
    return count


def result(inp):
    grid = solution(inp, False)
    return count_dots(grid)


def test(example_inp):
    assert result(example_inp) == 17
