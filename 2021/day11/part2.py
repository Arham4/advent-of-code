def in_limits(nums, y, x):
    if 0 <= y < len(nums) and 0 <= x < len(nums[0]):
        return True
    return False


flashes = 0
offsets = [
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
]

def print_pretty(nums):
    for line in nums:
        for num in line:
            print(num, end='')
        print()


def try_flash(nums, y, x, visited):
    global flashes
    if in_limits(nums, y, x) and (y, x) not in visited:
        nums[y][x] += 1
        if nums[y][x] >= 10:
            visited.add((y, x))
            nums[y][x] = 0
            flashes += 1
            for offset in offsets:
                try_flash(nums, y + offset[0], x + offset[1], visited)


def solution(inp):
    global flashes
    nums = []
    for line in inp:
        line_list = []
        for char in line:
            line_list.append(int(char))
        nums.append(line_list)

    answer = 0
    for i in range(2147000000):
        flashes_before = flashes
        visited = set()
        for y in range(len(inp)):
            for x in range(len(inp[0])):
                try_flash(nums, y, x, visited)
        if flashes - flashes_before == len(inp) * len(inp[0]):
            answer = i + 1
            break

    flashes = 0
    return answer


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 195
