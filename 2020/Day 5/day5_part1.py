lines = [line for line in open("input2.txt", "r")]

highest = 0
for line in lines:
    num = [0, 128]
    for i in range(7):
        c = line[i]
        avg = (num[0] + num[1]) // 2
        if c == "F":
            num[1] = avg
        elif c == "B":
            num[0] = avg
    num2 = [0, 8]
    for i in range(3):
        c = line[i + 7]
        avg = (num2[0] + num2[1]) // 2
        if c == "L":
            num2[1] = avg
        elif c == "R":
            num2[0] = avg
    seat_num = num[0] * 8 + num2[0]
    if seat_num > highest:
        highest = seat_num
print(highest)