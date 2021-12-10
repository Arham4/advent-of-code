matchings = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>'
}


points = {
    '}': 1197,
    ')': 3,
    ']': 57,
    '>': 25137,
}


def solution(inp):
    score = 0
    for line in inp:
        stack = []
        for char in line:
            if char == '{' or char == '(' or char == '[' or char == '<':
                stack.append(char)
            else:
                top = stack.pop()
                if char != matchings[top]:
                    score += points[char]
                    break
    return score


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 26397
