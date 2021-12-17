import parse


def in_range(position, x_min, x_max, y_min, y_max):
    return x_min <= position[0] <= x_max and y_min <= position[1] <= y_max


def solution(inp):
    pattern = "target area: x={x_min}..{x_max}, y={y_min}..{y_max}."
    match = parse.search(pattern, inp[0] + '.').named
    x_min, x_max, y_min, y_max = int(match['x_min']), int(match['x_max']), int(match['y_min']), int(match['y_max'])

    highest_y = -1000000000
    for x_try in range(x_max + 1):
        for y_try in range(y_min, abs(y_min) + 1):
            x_velocity = x_try
            y_velocity = y_try
            current_position = [0, 0]

            highest_sub_y = -1000000000
            while current_position[0] <= x_max and current_position[1] >= y_min:
                if in_range(current_position, x_min, x_max, y_min, y_max):
                    if highest_sub_y > highest_y:
                        highest_y = highest_sub_y
                    break

                current_position[0] += x_velocity
                current_position[1] += y_velocity

                if current_position[1] > highest_sub_y:
                    highest_sub_y = current_position[1]

                if x_velocity > 0:
                    x_velocity -= 1
                elif x_velocity < 0:
                    x_velocity += 1

                y_velocity -= 1

    return highest_y


def result(inp):
    return solution(inp)


def test(example_inp):
    assert result(example_inp) == 45
