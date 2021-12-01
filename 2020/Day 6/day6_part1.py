lines = [line.strip("\n") for line in open("input1.txt")]

sum = 0
s = []
person = 0
for line in lines:
    if line == "":
        sum += len(s)
        s = []
        person = 0
        continue
    for char in line:
        if person < len(s):
            s[person].append(char)
        else:
            s.append([char])
    person += 1
print(sum)