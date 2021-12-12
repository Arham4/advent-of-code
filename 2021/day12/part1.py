def add_mapping(mappings, by, to):
    if to != 'start' and by in mappings:
        mappings[by].append(to)
    elif to != 'start':
        mappings[by] = [to]


def go_from(mappings, at, path, path_disqualifier):
    if at == 'end':
        return 1

    if path_disqualifier(at, path):
        return 0

    new_path = path.copy()
    new_path.append(at)

    sub_result = 0
    for to in mappings[at]:
        sub_result += go_from(mappings, to, new_path, path_disqualifier)
    return sub_result


def lower_in_path(at, path):
    return at.islower() and at in path


def solution(inp):
    mappings = {}
    for line in inp:
        split = line.split('-')

        add_mapping(mappings, split[0], split[1])
        add_mapping(mappings, split[1], split[0])

    result = 0
    for to in mappings['start']:
        result += go_from(mappings, to, [], lower_in_path)

    return result


def result(inp):
    return solution(inp)


def test(example_inp1, example_inp2, example_inp3):
    assert result(example_inp1) == 10
    assert result(example_inp2) == 19
    assert result(example_inp3) == 226
