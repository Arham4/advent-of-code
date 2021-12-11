import part1


def solution(inp):
    nums = [[int(num) for num in line] for line in inp]

    steps = 0
    while True:
        visited = set()
        flashes_before = part1.flashes
        for y in range(len(inp)):
            for x in range(len(inp[0])):
                part1.try_flash(nums, y, x, visited)
        if part1.flashes - flashes_before == len(inp) * len(inp[0]):
            break
        steps += 1

    part1.flashes = 0
    return steps + 1


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 195
