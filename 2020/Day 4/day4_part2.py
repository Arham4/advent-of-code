import re

valids = [
    "byr:(1[0-9][2-9][0-9]|200[0-2])", 
    "iyr:(201[0-9]|2020)", 
    "eyr:(202[0-9]|2030)", 
    "hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)", 
    "hcl:#[0-9a-f]{6}( |\n)", 
    "ecl:(amb|blu|brn|gry|grn|hzl|oth)", 
    "pid:[0-9]{9}( |\n)"
]

def empty_array():
    global valids
    return [False for x in range(len(valids))]

has = empty_array()
lines = [line.strip("\n") + " " for line in open("input2.txt", "r")]
valid = 0
for line in lines:
    for i in range(len(valids)):
        reg = re.compile(r".*" + valids[i] + ".*")
        if reg.search(line):
            has[i] = True
    if line == " ":
        valid += 0 if False in has else 1
        has = empty_array()

valid += 0 if False in has else 1
print(valid)