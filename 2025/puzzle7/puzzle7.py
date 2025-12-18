#!/usr/bin/python3

f = open('input.txt')
#f = open('test.txt')
lines = f.read().splitlines()

def paths(width, height):
    grid = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(0)
        grid.append(row)

    for y in range(height):
        grid[y][0] = 1

    for x in range(width):
        grid[0][x] = 1

    for y in range(1, height):
        for x in range(1, width):
            grid[y][x] = grid[y-1][x] + grid[y][x-1]

    return grid[height-1][width-1]

def paths3d(width, height, depth):
    grid = []
    for _ in range(height):
        row = []
        for _ in range(width):
            line = []
            for _ in range(depth):
                line.append(0)
            row.append(line)
        grid.append(row)

    for y in range(height):
        grid[y][0][0] = 1

    for x in range(width):
        grid[0][x][0] = 1

    for z in range(depth):
        grid[0][0][z] = 1

    for y in range(1, height):
        for x in range(1, width):
            grid[y][x][0] = grid[y-1][x][0] + grid[y][x-1][0]

    for y in range(1, height):
        for z in range(1, depth):
            grid[y][0][z] = grid[y-1][0][z] + grid[y][0][z-1]

    for x in range(1, width):
        for z in range(1, depth):
            grid[0][x][z] = grid[0][x-1][z] + grid[0][x][z-1]

    for y in range(1, height):
        for x in range(1, width):
            for z in range(1, depth): 
                grid[y][x][z] = grid[y-1][x][z] + grid[y][x-1][z] + grid[y][x][z-1]

    return grid[height-1][width-1][depth-1]

total = 0
for line in lines:
    width, height = line.split()
    total += paths(int(width), int(height))
print(total)

total = 0
for line in lines:
    width, height = line.split()
    total += paths3d(int(width), int(height), int(width))
print(total)
