offsets = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]


def within_bounds(y, x, inp):
    return 0 <= y < len(inp) and 0 <= x < len(inp[0])


def find_lowest_points(inp):
    positions = []
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            least = True
            num = int(inp[y][x])
            for offset in offsets:
                near_y = y + offset[0]
                near_x = x + offset[1]
                if within_bounds(near_y, near_x, inp) and num >= int(inp[near_y][near_x]):
                    least = False
                    break
            if least:
                positions.append([y, x])
    return positions


def solution(inp):
    return sum([int(inp[pos[0]][pos[1]]) + 1 for pos in find_lowest_points(inp)])


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 15
