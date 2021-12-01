def solution(inp, offset):
    nums = [int(num) for num in inp]
    count = 0
    for previous, current in zip(nums, nums[offset:]):
        if current > previous:
            count += 1
    return count


def result(inp):
    return solution(inp, 1)


def test(example_inp):
    assert result(example_inp) == 7
