stripped_and_split = [line.strip("\n").split(": ") for line in open("input.txt", "r")]
all_lines = [[section[0].split(" "), section[1].split(" ")] for section in stripped_and_split]
yes = 0
for line in all_lines:
    positions = [int(num) for num in line[0][0].split("-")]
    
    index1 = positions[0] - 1
    index2 = positions[1] - 1
    char = line[0][1]
    password = line[1][0]
    yes += 1 if (password[index1] == char) ^ (password[index2] == char) else 0
print(yes)