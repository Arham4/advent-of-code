import json
import math


def depth(pairs):
    if isinstance(pairs, list):
        res = 1 + max(depth(pair) for pair in pairs)
        return res
    else:
        return 0


def add_num_or_split(pairs, index, number):
    pairs[index] += number
    if pairs[index] >= 10:
        print('new pair from', pairs[index], end='')
        pairs[index] = [int(math.floor(pairs[index] / 2)), int(math.ceil(pairs[index] / 2))]
        print(' is', pairs[index])


def try_again(full, full_indices, adding_numbers):
    if len(full_indices) > 1:
        for i in range(full_indices[0] + 1, len(full)):
            try_again(full[i], full_indices[1:], adding_numbers)
    else:
        for x in range(full_indices[0] + 1, len(full)):
            layer1 = full[x]
            print('try again layer1', layer1)
            if isinstance(layer1, list):
                for y in range(len(layer1)):
                    layer2 = layer1[y]
                    print('try again layer2', layer2)
                    if isinstance(layer2, list):
                        for i in range(len(layer2)):
                            layer3 = layer2[i]
                            print('try again layer3', layer3)
                            if adding_numbers is not None and isinstance(layer3, int):
                                print('add', adding_numbers[1], 'to', i, 'in layer2')
                                add_num_or_split(layer2, i, adding_numbers[1])
                                adding_numbers[1] = 0
                                break

                    if adding_numbers is not None and isinstance(layer2, int):
                        print('add', adding_numbers[1], 'to', y, 'in layer1')
                        add_num_or_split(layer1, y, adding_numbers[1])
                        adding_numbers[1] = 0
                        break

            if adding_numbers is not None and isinstance(layer1, int):
                print('add', adding_numbers[1], 'to', x, 'in full')
                add_num_or_split(full, x, adding_numbers[1])
                adding_numbers[1] = 0
                break


def explode(full, full_indices, pairs):
    adding_numbers = None
    indices = []
    for x in range(len(pairs)):
        layer1 = pairs[x]
        print('layer1', layer1)
        if isinstance(layer1, list):
            for y in range(len(layer1)):
                layer2 = layer1[y]
                print('layer2', layer2)
                if isinstance(layer2, list):
                    offset = 0
                    for i in range(len(layer2)):
                        layer3 = layer2[i - offset]
                        print('layer3', layer3)
                        if adding_numbers is None and isinstance(layer3, list):
                            print('boom')
                            indices = [x, y, i - offset]
                            layer2.remove(layer3)
                            adding_numbers = layer3
                            offset += 1
                        elif adding_numbers is not None and isinstance(layer3, list):
                            def recur(layer):
                                print('deep layer', layer)
                                for p in range(len(layer)):
                                    if isinstance(layer[p], list):
                                        recur(layer[p])
                                        break
                                    else:
                                        print('add', adding_numbers[1], 'to', p, layer[p], 'in deeper layer')
                                        add_num_or_split(layer, p, adding_numbers[1])
                                        adding_numbers[1] = 0
                                        break
                            recur(layer3)
                            break
                        if adding_numbers is not None and isinstance(layer3, int):
                            print('add', adding_numbers[1], 'to', i - offset, 'in layer2')
                            add_num_or_split(layer2, i - offset, adding_numbers[1])
                            adding_numbers[1] = 0
                            break
                if adding_numbers is not None and isinstance(layer2, int):
                    print('add', adding_numbers[1], 'to', y, 'in layer1')
                    add_num_or_split(layer1, y, adding_numbers[1])
                    adding_numbers[1] = 0
                    break
        if adding_numbers is not None and isinstance(layer1, int):
            print('add', adding_numbers[1], 'to', x, 'in pairs')
            add_num_or_split(pairs, x, adding_numbers[1])
            adding_numbers[1] = 0
            break

    for x in reversed(range(indices[0] + 1)):
        layer1 = pairs[x]
        print('reverse layer1', layer1)
        if isinstance(layer1, list):
            for y in reversed(range(indices[1] + 1)):
                layer2 = layer1[y]
                print('reverse layer2', layer2)
                if isinstance(layer2, list):
                    for i in reversed(range(indices[2])):
                        layer3 = layer2[i]
                        print('reverse layer3', layer3)
                        if adding_numbers is not None and isinstance(layer3, int):
                            print('add', adding_numbers[0], 'to', i, 'in layer3')
                            add_num_or_split(layer2, i, adding_numbers[0])
                            adding_numbers[0] = 0
                            break

    for x in reversed(range(indices[0])):
        layer1 = pairs[x]
        print('reverse layer1', layer1)
        if isinstance(layer1, list):
            for y in reversed(range(indices[1])):
                layer2 = layer1[y]
                print('reverse layer2', layer2)
                if adding_numbers is not None and isinstance(layer2, list):
                    def recur(layer):
                        print('reverse deep layer', layer)
                        for p in reversed(range(len(layer))):
                            if isinstance(layer[p], list):
                                recur(layer[p])
                                break
                            else:
                                print('add', adding_numbers[0], 'to', p, layer[p], 'in reverse deeper layer')
                                add_num_or_split(layer, p, adding_numbers[0])
                                adding_numbers[0] = 0
                                break
                    recur(layer2)
                    break
                if adding_numbers is not None and isinstance(layer2, int):
                    print('add', adding_numbers[0], 'to', y, 'in layer2')
                    add_num_or_split(layer1, y, adding_numbers[0])
                    adding_numbers[0] = 0
                    break

    for x in reversed(range(indices[0])):
        layer1 = pairs[x]
        print('reverse layer1', layer1)
        if adding_numbers is not None and isinstance(layer1, int):
            print('add', adding_numbers[0], 'to', x, layer1, 'in layer1')
            add_num_or_split(pairs, x, adding_numbers[0])
            adding_numbers[0] = 0
            break

    pairs[indices[0]][indices[1]].insert(indices[2], 0)

    if adding_numbers[1] != 0:
        try_again(full, full_indices.copy(), adding_numbers)

    print('leftover nums', adding_numbers)

def reduce(full, indices, pairs):
    print(pairs, 'has depth', depth(pairs))
    if depth(pairs) > 4:
        while depth(pairs) > 4:
            for i in range(len(pairs)):
                pair = pairs[i]
                if depth(pair) >= 4:
                    indices_new = indices.copy()
                    indices_new.append(i)

                    reduce(full, indices, pair)
    elif depth(pairs) == 4:
        print('explode', pairs)
        explode(full, indices, pairs)
        print('result', pairs)


def magnitude(pairs):
    if isinstance(pairs, int):
        return pairs
    return magnitude(pairs[0]) * 3 + magnitude(pairs[1]) * 2


def solution(inp):
    pairs = [json.loads(inp[0])]
    for i in range(1, len(inp)):
        pairs.append(json.loads(inp[i]))
        print(pairs)

        reduce(pairs, [0], pairs)

    print('final', pairs)
    print('magnitude', magnitude(pairs))

def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 3488
