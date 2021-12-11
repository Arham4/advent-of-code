flashes = 0


def in_limits(nums, y, x):
    return 0 <= y < len(nums) and 0 <= x < len(nums[0])


def try_flash(nums, y, x, visited):
    global flashes
    if in_limits(nums, y, x) and (y, x) not in visited:
        nums[y][x] += 1
        if nums[y][x] >= 10:
            visited.add((y, x))
            nums[y][x] = 0
            flashes += 1
            for y2 in range(y - 1, y + 2):
                for x2 in range(x - 1, x + 2):
                    try_flash(nums, y2, x2, visited)


def solution(inp):
    global flashes
    nums = [[int(num) for num in line] for line in inp]

    for i in range(100):
        visited = set()
        for y in range(len(inp)):
            for x in range(len(inp[0])):
                try_flash(nums, y, x, visited)

    answer = flashes
    flashes = 0 # by the way this line cost me 40 minutes of my life
    return answer


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 1656
