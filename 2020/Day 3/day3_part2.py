from functools import reduce

graph = [line.strip("\n") for line in open("input-1.txt", "r")]
slope_groups = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_per_slope = []

for slopes in slope_groups:
    x = 0
    trees = 0
    for y in range(0, len(graph), slopes[1]):
        if graph[y][x] == "#":
            trees += 1
        x = (x + slopes[0]) % len(graph[0])
    trees_per_slope.append(trees)
    
print(reduce(lambda x, y: x * y, trees_per_slope))