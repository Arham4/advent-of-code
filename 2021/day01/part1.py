def result(inp):
    return result2(inp, 1)


def result2(inp, offset):
    nums = [int(num) for num in inp]
    count = 0
    for previous, current in zip(nums, nums[offset:]):
        if current > previous:
            count += 1
    return count


def test(example_inp):
    assert result(example_inp) == 7
