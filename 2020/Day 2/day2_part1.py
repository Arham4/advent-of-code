stripped_and_split = [line.strip("\n").split(": ") for line in open("input.txt", "r")]
all_lines = [[section[0].split(" "), section[1].split(" ")] for section in stripped_and_split]
yes = 0
for line in all_lines:
    range = [int(num) for num in line[0][0].split("-")]
    
    min_num = range[0]
    max_num = range[1]
    char = line[0][1]
    password = line[1][0]
    count = password.count(char)
    
    if count >= min_num and count <= max_num:
        yes += 1
print(yes)