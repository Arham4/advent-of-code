def slope_of(left, right):
    return 1 if right > left else 0 if right == left else -1


def mark_map(map, y, x):
    if y not in map:
        map[y] = {}

    if x in map[y]:
        map[y][x] += 1
    else:
        map[y][x] = 1


def solution(inp, horizontal_only):
    map = {}
    for line in inp:
        split = line.split(' -> ')
        left = [int(num) for num in split[0].split(',')]
        right = [int(num) for num in split[1].split(',')]

        if horizontal_only and left[0] != right[0] and left[1] != right[1]:
            continue

        slopes = [slope_of(left[0], right[0]), slope_of(left[1], right[1])]
        current_pos = [left[0], left[1]]

        while current_pos[0] != float(right[0]) or current_pos[1] != float(right[1]):
            mark_map(map, current_pos[1], current_pos[0])

            current_pos = [pos + slope for pos, slope in zip(current_pos, slopes)]

        mark_map(map, current_pos[1], current_pos[0])

    return sum([sum(hits >= 2 for hits in y.values()) for y in map.values()])


def result(inp):
    return solution(inp, True)


def test(example_inp):
    assert result(example_inp) == 5
