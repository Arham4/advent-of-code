import part1


def solution(inp):
    nums_to_call = inp[0].split(',')
    squares = []
    offset = 0
    for i in range(0, len(inp), 5):
        square = part1.Square()
        square.make_grid(inp[i + offset + 2:i + offset + 7])
        offset += 1
        if square.grid:
            squares.append(square)
    squares_finished = [False] * len(squares)
    for num in nums_to_call:
        for i in range(len(squares)):
            square = squares[i]
            square.mark(num)
            squares_finished[i] = square.finished()
            if all(squares_finished):
                return square.sum_unmarked() * int(num)


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 1924
