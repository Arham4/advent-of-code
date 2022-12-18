from typing import List, Tuple, Set


def shift_right(rock: List[Tuple[int, int]], coordinates: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
    amount = 1

    x = [x for x, y in rock]
    highest_x = max(x)

    right = [(x + amount, y) for x, y in rock]
    if highest_x + 1 > 6 or any([r in coordinates for r in right]):
        amount = 0

    return [(x + amount, y) for x, y in rock]


def shift_left(rock: List[Tuple[int, int]], coordinates: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
    amount = 1

    x = [x for x, y in rock]
    lowest_x = min(x)

    left = [(x - amount, y) for x, y in rock]
    if lowest_x - 1 < 0 or any([l in coordinates for l in left]):
        amount = 0

    return [(x - amount, y) for x, y in rock]


def shift_direction(rock: List[Tuple[int, int]], direction: str, coordinates: Set[Tuple[int, int]]) -> List[
    Tuple[int, int]]:
    if direction == '>':
        return shift_right(rock, coordinates)
    elif direction == '<':
        return shift_left(rock, coordinates)


def shift_up(rock: List[Tuple[int, int]], amount: int) -> List[Tuple[int, int]]:
    return [(x, y + amount) for x, y in rock]


def shift_down(rock: List[Tuple[int, int]], amount: int) -> List[Tuple[int, int]]:
    return [(x, y - amount) for x, y in rock]


def get_highest_y_coord(coordinates: List[Tuple[int, int]]) -> int:
    y = [y for x, y in coordinates]
    if len(y) == 0:
        return 0
    return max(y)


def reached_bottom(rock: List[Tuple[int, int]], coordinates: Set[Tuple[int, int]]) -> bool:
    for loc in rock:
        x, y = loc
        if y == 0 or loc in coordinates:
            return True
    return False


def add_coordinates(coordinates: Set[Tuple[int, int]], rock: List[Tuple[int, int]]) -> None:
    for x, y in rock:
        coordinates.add((x, y))


def solution(inp: List[str]) -> int:
    inp = inp[0]

    direction = 0
    rock = 0
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
    ]
    coordinates = set()

    # rocks[0] = ####

    # rocks[1] = .#.
    #            ###
    #            .#.

    # rocks[2] = ..#
    #            ..#
    #            ###

    # rocks[3] = #
    #            #
    #            #
    #            #

    # rocks[4] = ##
    #            ##

    highest_y_coord = 0

    for _ in range(2022):
        current_rock = rocks[rock].copy()
        current_rock = shift_up(current_rock, highest_y_coord + 4)
        for i in range(2):
            current_rock = shift_right(current_rock, coordinates)

        rock_not_placed = True

        while rock_not_placed:
            current_direction = inp[direction]
            current_rock = shift_direction(current_rock, current_direction, coordinates)
            direction = (direction + 1) % len(inp)

            down = shift_down(current_rock, 1)
            if reached_bottom(down, coordinates):
                rock_not_placed = False
                add_coordinates(coordinates, current_rock)
                highest_y_coord = max(highest_y_coord, max([y for x, y in current_rock]))
            else:
                current_rock = down

        rock = (rock + 1) % len(rocks)
    return highest_y_coord


def result(inp: List[str]) -> int:
    return solution(inp)


def test(examples: List[List[str]]) -> None:
    example = 0
    exp = 3068
    res = result(examples[example])
    assert res == exp, f"example {example}: result was {res}, expected {exp}"
