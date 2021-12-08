import part1


def construct_freq_table(word):
    freq_table = {}
    for letter in word:
        if letter not in freq_table:
            freq_table[letter] = 1
        else:
            freq_table[letter] += 1
    return freq_table


def matches(freq_table, word):
    if len(freq_table) != len(word):
        return False
    for letter in word:
        if letter not in freq_table:
            return False
    return True


def decode_number(freq_table, base_words):
    for pair in base_words:
        if matches(freq_table, pair[0]):
            return pair[1]
    raise Exception('Could not decode number ' + str(freq_table))


def replace(string, to_replace):
    for c in to_replace:
        string = string.replace(c, '')
    return string


def construct_base_words(left):
    base_words = {}
    result = []
    for word in left:
        if len(word) == 2:
            base_words[1] = word
            result.append([word, 1])
        elif len(word) == 3:
            base_words[7] = word
            result.append([word, 7])
        elif len(word) == 4:
            base_words[4] = word
            result.append([word, 4])
        elif len(word) == 7:
            base_words[8] = word
            result.append([word, 8])

    top_right = base_words[1][0]
    bottom_right = base_words[1][1]

    top = replace(base_words[7], base_words[1])

    top_left = replace(base_words[4], base_words[1])[1]
    middle = replace(base_words[4], base_words[1])[0]

    bottom_left = replace(replace(base_words[8], base_words[7]), base_words[4])[1]
    bottom = replace(replace(base_words[8], base_words[7]), base_words[4])[0]

    result.append([top + top_left + top_right + bottom_left + bottom_right + bottom, 0])
    result.append([top + middle + top_right + bottom_left + bottom_right + bottom, 0])

    result.append([top + top_right + middle + bottom_left + bottom, 2])
    result.append([top + bottom_right + middle + bottom_left + bottom, 2])
    result.append([top + top_right + top_left + bottom_left + bottom, 2])
    result.append([top + bottom_right + top_left + bottom_left + bottom, 2])

    result.append([top + top_right + middle + bottom_right + bottom_left, 3])
    result.append([top + top_right + top_left + bottom_right + bottom_left, 3])
    result.append([top + top_right + middle + bottom_right + bottom, 3])
    result.append([top + top_right + top_left + bottom_right + bottom, 3])

    result.append([top + top_left + middle + bottom_right + bottom, 5])
    result.append([top + top_left + middle + top_right + bottom, 5])
    result.append([top + top_left + middle + bottom_right + bottom_left, 5])
    result.append([top + top_left + middle + top_right + bottom_left, 5])

    result.append([top + top_left + middle + bottom_left + bottom_right + bottom, 6])
    result.append([top + top_left + middle + bottom_left + top_right + bottom, 6])

    result.append([top + top_left + top_right + middle + bottom_right + bottom, 9])
    result.append([top + top_left + top_right + middle + bottom_right + bottom_left, 9])
    return result


def solution(inp):
    entries = [[segment.split(' | ')[0].split(' '), segment.split(' | ')[1].split(' ')] for segment in inp]
    nums = []
    for entry in entries:
        left = entry[0]
        right = entry[1]
        freq_tables = []
        base_words = construct_base_words(left)
        for word in left:
            freq_table = construct_freq_table(word)
            number = decode_number(freq_table, base_words)
            freq_tables.append([freq_table, number])

        right_num_raw = ''
        for word in right:
            freq_table = construct_freq_table(word)
            for other_table in freq_tables:
                passed = True
                if len(freq_table) != len(other_table[0]):
                    passed = False
                else:
                    for key, value in other_table[0].items():
                        if key not in freq_table or freq_table[key] != value:
                            passed = False
                            break
                    for key, value in freq_table.items():
                        if key not in other_table[0] or other_table[0][key] != value:
                            passed = False
                            break

                if passed:
                    right_num_raw += str(other_table[1])
        nums.append(int(right_num_raw))
    return sum(nums)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 61229
