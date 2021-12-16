from functools import reduce
import part1


def parse_binary(binary):
    type_id = int(binary[3:6], 2)

    rest_of_binary = binary[6:]

    if type_id == 4:
        length, literal = part1.parse_literal(rest_of_binary)
        return literal, 6 + length
    else:
        length_type_id = rest_of_binary[0]
        if length_type_id == '0':
            length, values = part1.parse_fixed_length(rest_of_binary[1:], parse_binary)
        else:
            length, values = part1.parse_variable_length(rest_of_binary[1:], parse_binary)

        if type_id == 0:
            return sum(values), 7 + length
        elif type_id == 1:
            return reduce(lambda x, y: x * y, values), 7 + length
        elif type_id == 2:
            return min(values), 7 + length
        elif type_id == 3:
            return max(values), 7 + length
        elif type_id == 5:
            return 1 if values[0] > values[1] else 0, 7 + length
        elif type_id == 6:
            return 1 if values[0] < values[1] else 0, 7 + length
        elif type_id == 7:
            return 1 if values[0] == values[1] else 0, 7 + length


def solution(inp):
    binary = part1.hex_to_full_bin(inp[0])
    return parse_binary(binary)[0]


def result(inp):
    return solution(inp)


def test(example_inp8, example_inp9, example_inp10, example_inp11, example_inp12, example_inp13, example_inp14, example_inp15):
    assert result(example_inp8) == 3
    assert result(example_inp9) == 54
    assert result(example_inp10) == 7
    assert result(example_inp11) == 9
    assert result(example_inp12) == 1
    assert result(example_inp13) == 0
    assert result(example_inp14) == 0
    assert result(example_inp15) == 1
