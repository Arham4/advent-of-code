import json
import math


class Number:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        '''repr = '(value=' + str(self.value)
        if self.left is not None:
            repr += ', left=' + str(self.left.value)
        else:
            repr += ', left=None'

        if self.right is not None:
            repr += ', right=' + str(self.right.value)
        else:
            repr += ', right=None'

        repr += ')'
        return repr
        '''
        return str(self.value)


def depth(pairs):
    if isinstance(pairs, list):
        res = 1 + max(depth(pair) for pair in pairs)
        return res
    else:
        return 0


def convert_numbers(item):
    for l in range(len(item)):
        if isinstance(item[l], int):
            item[l] = Number(item[l])
        elif isinstance(item[l], list):
            convert_numbers(item[l])


def make_neighbors(item):
    aggregated = []

    def visit_all(item):
        for l in range(len(item)):
            if isinstance(item[l], Number):
                aggregated.append(item[l])
            elif isinstance(item[l], list):
                visit_all(item[l])

    visit_all(item)

    aggregated[0].right = aggregated[1]
    aggregated[-1].left = aggregated[-2]
    for i in range(1, len(aggregated) - 1):
        aggregated[i].left = aggregated[i - 1]
        aggregated[i].right = aggregated[i + 1]


def read_line(line):
    line_to_list = json.loads(line)
    for l in range(len(line_to_list)):
        convert_numbers(line_to_list)
    return line_to_list


def split(pairs):
    for l in range(len(pairs)):
        if isinstance(pairs[l], Number):
            previous_number = pairs[l]

            if pairs[l].value >= 10:

                half = pairs[l].value / 2
                pairs[l] = [Number(int(math.floor(half))), Number(int(math.ceil(half)))]

                pairs[l][0].left = previous_number.left
                pairs[l][0].right = pairs[l][1]
                if previous_number.left is not None:
                    previous_number.left.right = pairs[l][0]

                pairs[l][1].left = pairs[l][0]
                pairs[l][1].right = previous_number.right
                if previous_number.right is not None:
                    previous_number.right.left = pairs[l][1]

                return True
        elif isinstance(pairs[l], list):
            if split(pairs[l]):
                return True
    return False


def is_number_pair(pairs):
    for item in pairs:
        if isinstance(item, list):
            return False
    return True


def explode(full, pairs, depth):
    if isinstance(pairs, list):
        if depth >= 3:
            for i in range(len(pairs)):
                layer3 = pairs[i]
                if isinstance(pairs[i], list):
                    if is_number_pair(pairs[i]):
                        pairs.remove(layer3)

                        replacement = Number(0)
                        if layer3[0].left is not None:
                            replacement.left = layer3[0].left

                            layer3[0].left.right = replacement
                            layer3[0].left.value += layer3[0].value

                        if layer3[1].right is not None:
                            replacement.right = layer3[1].right

                            layer3[1].right.left = replacement
                            layer3[1].right.value += layer3[1].value

                        pairs.insert(i, replacement)
                        return True
                    elif explode(full, pairs[i], depth + 1):
                        return True
        else:
            for item in pairs:
                if explode(full, item, depth + 1):
                    return True
    return False


def reduce(full, indices, pairs):
    if depth(pairs) > 4:
        while depth(pairs) > 4:
            for i in range(len(pairs)):
                pair = pairs[i]
                if depth(pair) >= 4:
                    indices_new = indices.copy()
                    indices_new.append(i)

                    reduce(full, indices, pair)
                    
            split(full)
    else:
        while True:
            if explode(full, pairs, 1):
                pass
            elif split(pairs):
                pass
            else:
                break


def magnitude(pairs):
    if isinstance(pairs, Number):
        return pairs.value
    return magnitude(pairs[0]) * 3 + magnitude(pairs[1]) * 2


def solution(inp):
    pairs = read_line(inp[0])
    for i in range(1, len(inp)):
        pairs = [pairs, read_line(inp[i])]
        make_neighbors(pairs)

        reduce(pairs, [0], pairs)
    return magnitude(pairs)

def result(inp):
    return solution(inp)


def test(example_inp):
    print('answer', result(example_inp))
    assert result(example_inp) == 3488
