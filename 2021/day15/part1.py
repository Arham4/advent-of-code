def wrap_num(num, offset):
    new_num = num + offset
    if new_num > 9:
        return new_num - 9
    return new_num


def in_bounds(inp, expansions, y, x):
    return 0 <= y < len(inp) * expansions and 0 <= x < len(inp[0]) * expansions


def solution(inp, expansions):
    maze = [[0] * (len(inp[0]) * expansions) for _ in (inp * expansions)]
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            value = int(inp[y][x])
            for y2 in range(expansions):
                for x2 in range(expansions):
                    pos = (y + len(inp) * y2, x + len(inp[0]) * x2)
                    maze[pos[0]][pos[1]] = wrap_num(value, y2 + x2)

    dp = [[214700000000000000] * (len(inp[0]) * expansions) for _ in (inp * expansions)]
    while True:
        before = dp[len(dp) - 1][len(dp[0]) - 1]

        for y in range(len(maze)):
            for x in range(len(maze[0])):
                found = False
                above = 214700000000000000
                if in_bounds(inp, expansions, y - 1, x):
                    above = dp[y - 1][x]
                    if above == 214700000000000000:
                        above = int(inp[y - 1][x])
                    found = True

                left = 214700000000000000
                if in_bounds(inp, expansions, y, x - 1):
                    left = dp[y][x - 1]
                    if left == 214700000000000000:
                        left = int(inp[y][x - 1])
                    found = True

                bottom = 214700000000000000
                if in_bounds(inp, expansions, y + 1, x):
                    bottom = dp[y + 1][x]
                    found = True

                right = 214700000000000000
                if in_bounds(inp, expansions, y, x + 1):
                    right = dp[y][x + 1]
                    found = True

                smallest = min(above, left, bottom, right)
                if y == 0 and x == 0 or not found:
                    dp[y][x] = 0
                else:
                    dp[y][x] = maze[y][x] + smallest

        if dp[len(dp) - 1][len(dp[0]) - 1] == before:
            break

    return dp[len(dp) - 1][len(dp[0]) - 1]


def result(inp):
    return solution(inp, 1)


def test(example_inp):
    assert result(example_inp) == 40
