from collections import Counter


def solution(inp, steps):
    init = inp[0]
    sequences = {line[0] + line[1]: line[6] for line in inp if '->' in line}

    counts = Counter()
    for i in range(len(init) - 1):
        current = init[i]
        next = init[i + 1]

        counts[current + next] += 1

    for x in range(steps):
        new_counts = counts.copy()
        for count in counts:
            if count in sequences:
                new_counts[count[0] + sequences[count]] += counts[count]
                new_counts[sequences[count] + count[1]] += counts[count]

                new_counts[count] -= counts[count]

        counts = new_counts

    beginnings = Counter()
    ends = Counter()
    for count in counts:
        beginnings[count[0]] += counts[count]
        ends[count[1]] += counts[count]

    res = Counter()
    for letter in set(beginnings).union(ends):
        count = max(beginnings.get(letter, 0), ends.get(letter, 0))
        res[letter] = count

    ordered = res.most_common()
    return ordered[0][1] - ordered[-1][1]


def result(inp):
    return solution(inp, 10)


def test(example_inp):
    assert result(example_inp) == 1588
