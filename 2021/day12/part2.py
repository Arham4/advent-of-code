import part1


def any_lowers_visited_twice(path):
    visited = set()
    for location in [location for location in path if location.islower()]:
        if location in visited:
            return True
        else:
            visited.add(location)
    return False


def lower_is_not_exception(at, path):
    return at.islower() and ((any_lowers_visited_twice(path) and at in path) or path.count(at) == 2)


def solution(inp):
    mappings = {}
    for line in inp:
        split = line.split('-')

        part1.add_mapping(mappings, split[0], split[1])
        part1.add_mapping(mappings, split[1], split[0])

    result = 0
    for to in mappings['start']:
        result += part1.go_from(mappings, to, [], lower_is_not_exception)

    return result


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 36
