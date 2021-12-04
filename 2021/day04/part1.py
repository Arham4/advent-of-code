class Mark:
    def __init__(self, mark):
        self.mark = mark
        self.marked = False

    def glow(self):
        self.marked = True


class Square:
    def __init__(self):
        self.grid = []

    def make_grid(self, lines):
        self.grid = []
        for line in lines:
            self.grid.append([Mark(num) for num in line.strip().replace('  ', ' ').split(' ')])

    def mark(self, num):
        for lines in self.grid:
            for i in range(len(lines)):
                if lines[i].mark == num:
                    lines[i].glow()
                    return

    def finished(self):
        finished_2 = [True] * len(self.grid[0])
        for line in self.grid:
            finished = True
            for i in range(len(line)):
                num = line[i]
                if not num.marked:
                    finished = False
                    finished_2[i] = False
            if finished:
                return True
        return any(finished_2)

    def sum_unmarked(self):
        sum = 0
        for line in self.grid:
            for num in line:
                if not num.marked:
                    sum += int(num.mark)
        return sum


def solution(inp):
    nums_to_call = inp[0].split(',')
    squares = []
    offset = 0
    for i in range(0, len(inp), 5):
        square = Square()
        square.make_grid(inp[i + offset + 2:i + offset + 7])
        offset += 1
        if square.grid:
            squares.append(square)
    for num in nums_to_call:
        for square in squares:
            square.mark(num)
            if square.finished():
                return square.sum_unmarked() * int(num)
    return 0


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 4512
