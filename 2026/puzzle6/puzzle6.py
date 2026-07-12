#!/usr/bin/python3

def find_start(grid):
    for y in range(0, height):
        for x in range(0, width):
            if grid[y][x] == 'S':
                return x, y

def in_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

def rotate(grid, x, y):
    direction = grid[y][x]
    opposite = ""
    if direction == "L":
        opposite = "R"
    elif direction == "R":
        opposite = "L"

    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if in_bounds(nx, ny):
            if grid[ny][nx] == "#":
                grid[ny][nx] = opposite
                rotate(grid, nx, ny)
            elif grid[ny][nx] == "*":
                if direction == "R":
                    grid[ny][nx] = "1"
                elif direction == "L":
                    grid[ny][nx] = "0"
            elif grid[ny][nx] == "0" and direction == "R":
                grid[ny][nx] = "1"

def get_num(grid):
    digits = []
    for y in range(0, height):
        for x in range(0, width):
            if grid[y][x] == "0" or grid[y][x] == "1":
                digits.append(grid[y][x])

    return int("".join(digits), 2)

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

grid = []
for line in open('input.txt').read().splitlines():
    grid.append(list(line))
height = len(grid)
width = len(grid[0])

x, y = find_start(grid)
grid[y][x] = "L"
rotate(grid, x, y)

print(get_num(grid))
