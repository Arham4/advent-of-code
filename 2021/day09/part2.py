import part1

offsets = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]


def sprawl(inp, y, x, visited):
    if part1.within_bounds(y, x, inp) and int(inp[y][x]) != 9 and (y, x) not in visited:
        visited.add((y, x))
        return 1 + sum([sprawl(inp, y + offset[0], x + offset[1], visited) for offset in offsets])
    return 0


def solution(inp):
    lowest_points = part1.find_lowest_points(inp)
    sizes = [max([sprawl(inp, origin[0] + offset[0], origin[1] + offset[1], set()) for offset in offsets])
             for origin in lowest_points]
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 1134
