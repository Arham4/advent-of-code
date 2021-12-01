lines = [line.strip("\n") for line in open("input2.txt")]

sum = 0
chars = set()
s = []
person = 0
for line in lines:
    if line == "":
        total_count = len(s)
        in_all = [c for c in chars]
        for char in chars:
            for p in s:
                if char not in p:
                    in_all.remove(char)
                    break
        if in_all:
            sum += len(in_all)
        s = []
        chars = set()
        person = 0
        continue
    for char in line:
        if person < len(s):
            s[person].append(char)
        else:
            s.append([char])
        chars.add(char)
    person += 1
    
print(sum)