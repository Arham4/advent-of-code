import part1


def result(inp):
    nums = [int(num) for num in inp]
    count = 0
    for previous, current in zip(nums, nums[3:]):
        if current > previous:
            count += 1
    return count


def test(example_inp):
    assert result(example_inp) == 5
