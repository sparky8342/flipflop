#!/usr/bin/python3

f = open('input.txt')
lines = f.read().splitlines()

def paths(width, height):
    grid = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(0)
        grid.append(row)

    for x in range(width):
        grid[0][x] = 1

    for y in range(height):
        grid[y][0] = 1

    for y in range(1, height):
        for x in range(1, width):
            grid[y][x] = grid[y-1][x] + grid[y][x-1]

    return grid[height-1][width-1]

total = 0
for line in lines:
    width, height = line.split()
    total += paths(int(width), int(height))
print(total)
