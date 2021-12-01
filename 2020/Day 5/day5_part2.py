lines = [line for line in open("input1.txt", "r")]
valids = [False] * 929 # assumption: 928 is highest seat id

def get_binary_partition(low_num, high_num, line, end_index, front_char, back_char, initial_index=0):
    num = [low_num, high_num]
    for i in range(end_index):
        c = line[i + initial_index]
        avg = (num[0] + num[1]) // 2
        if c == front_char:
            num[1] = avg
        elif c == back_char:
            num[0] = avg
    return num[0]

first_true = len(valids)
for line in lines:
    row = get_binary_partition(0, 128, line, 7, 'F', 'B')
    column = get_binary_partition(0, 8, line, 3, 'L', 'R', 7)
    seat_num = row * 8 + column
    valids[seat_num] = True
    if valids[seat_num] and seat_num < first_true:
        first_true = seat_num

first_false_since = 0
for i in range(first_true, len(valids)):
    if not valids[i]:
        first_false_since = i
        break

print(first_false_since)