valids = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

def empty_array():
    global valids
    return [False for x in range(len(valids))]

has = empty_array()
lines = [line.strip("\n") for line in open("input2.txt", "r")]
valid = 0
for line in lines:
    for i in range(len(valids)):
        if valids[i] in line:
            has[i] = True
    if line == "":
        valid += 0 if False in has else 1
        has = empty_array()

print(valid)