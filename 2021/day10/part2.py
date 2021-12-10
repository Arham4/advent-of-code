rewards = {
    '{': ['}', 3],
    '(': [')', 1],
    '[': [']', 2],
    '<': ['>', 4],
}


def solution(inp):
    scores = []
    for line in inp:
        points = 0
        stack = []
        consider = True
        for char in line:
            if char in rewards:
                stack.append(char)
            else:
                top = stack.pop()
                if char != rewards[top][0]:
                    consider = False
                    break
        if consider:
            for fault in reversed(stack):
                points = points * 5 + rewards[fault][1]
            scores.append(points)
    scores.sort()
    return scores[len(scores) // 2]


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 288957
