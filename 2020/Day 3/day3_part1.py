graph = [line.strip("\n") for line in open("input-1.txt", "r")]
x = 0
trees = 0
for y in range(len(graph)):
    if graph[y][x] == "#":
        trees += 1
    x = (x + 3) % len(graph[0])
print(trees)