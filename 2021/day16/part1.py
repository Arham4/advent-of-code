def hex_to_full_bin(num):
    binary = ''
    for digit in num:
        binary += bin(int(digit, 16))[2:].zfill(4)
    return binary


def parse_literal(binary):
    literal_index = 0
    literals = ''
    while True:
        sub_group = binary[literal_index:literal_index + 5]
        literal_index += 5

        literals += sub_group[1:]

        if sub_group[0] == '0':
            break

    literal = int(literals, 2)
    return literal_index, literal


def parse_fixed_length(binary, subsection_parser):
    length = int(binary[0:15], 2)
    binary_remaining = binary[15:15 + length]

    values = []
    parsed_index = 0
    while parsed_index < length:
        value, amount_parsed = subsection_parser(binary_remaining[parsed_index:])
        parsed_index += amount_parsed
        values.append(value)

    return 15 + length, values


def parse_variable_length(binary, subsection_parser):
    sub_packets = int(binary[0:11], 2)
    binary_remaining = binary[11:]

    values = []
    parsed_index = 0
    processed = 0
    while processed < sub_packets:
        value, amount_parsed = subsection_parser(binary_remaining[parsed_index:])
        parsed_index += amount_parsed
        values.append(value)

        processed += 1

    return 11 + parsed_index, values


def parse_binary(binary):
    packet_version = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)

    rest_of_binary = binary[6:]

    if type_id == 4:
        length, literal = parse_literal(rest_of_binary)
        return packet_version, 6 + length
    else:
        length_type_id = rest_of_binary[0]
        if length_type_id == '0':
            length, values = parse_fixed_length(rest_of_binary[1:], parse_binary)
            return packet_version + sum(values), 7 + length
        else:
            length, values = parse_variable_length(rest_of_binary[1:], parse_binary)
            return packet_version + sum(values), 7 + length


def solution(inp):
    binary = hex_to_full_bin(inp[0])
    return parse_binary(binary)[0]


def result(inp):
    return solution(inp)


def test(example_inp1, example_inp2, example_inp3, example_inp4, example_inp5, example_inp6, example_inp7):
    assert result(example_inp1) == 6
    assert result(example_inp2) == 9
    assert result(example_inp3) == 14
    assert result(example_inp4) == 16
    assert result(example_inp5) == 12
    assert result(example_inp6) == 23
    assert result(example_inp7) == 31
