import part1


points = {
    '{': 3,
    '(': 1,
    '[': 2,
    '<': 4,
}


def solution(inp):
    scores = []
    for line in inp:
        score = 0
        stack = []
        consider = True
        for char in line:
            if char in part1.matchings:
                stack.append(char)
            else:
                top = stack.pop()
                if char != part1.matchings[top]:
                    consider = False
                    break
        if consider:
            for fault in reversed(stack):
                score = score * 5 + points[fault]
            scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 288957
