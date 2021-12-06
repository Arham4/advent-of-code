def solution(inp, count):
    fish = [[int(num), 1] for num in inp[0].split(',')]
    for i in range(count):
        to_add = sum([nums[1] for nums in fish if nums[0] == 0])
        fish = [[num[0] - 1, num[1]] if num[0] > 0 else [6, num[1]] for num in fish]
        if to_add > 0:
            fish.append([8, to_add])
    return sum([nums[1] for nums in fish])


def result(inp):
    return solution(inp, 80)


def test(example_inp):
    assert result(example_inp) == 5934
