def in_bounds(inp, y, x):
    return 0 <= y < len(inp) and 0 <= x < len(inp[0])


def smallest_dist(to_visit, dist):
    smallest_value = 100000000
    smallest_key = None
    for current in to_visit:
        if dist[current] < smallest_value:
            smallest_value = dist[current]
            smallest_key = current
    return smallest_key


def solution(inp):
    to_visit = set()

    dist = {}

    for y in range(len(inp)):
        for x in range(len(inp[0])):
            dist[(y, x)] = 10000000
            to_visit.add((y, x))

    dist[(0, 0)] = 0

    while len(to_visit) > 0:
        current = smallest_dist(to_visit, dist)

        to_visit.remove(current)

        for offset in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next = (current[0] + offset[0], current[1] + offset[1])
            if in_bounds(inp, next[0], next[1]) and next in to_visit:
                this_dist = dist[current] + int(inp[next[0]][next[1]])
                if this_dist < dist[next]:
                    dist[next] = this_dist

    return dist[(len(inp) - 1, len(inp[0]) - 1)]


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 40
