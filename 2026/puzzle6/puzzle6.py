#!/usr/bin/python3

def clone(grid):
    cl = [row[:] for row in grid]
    return cl

def find_start(grid):
    for y in range(0, height):
        for x in range(0, width):
            if grid[y][x] == 'S':
                return x, y

def in_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

def rotate(grid, x, y, direction, visited, outputs):
    pos = (x, y)
    if pos in visited:
        return
    visited.add(pos)

    opposite = "L" if direction == "R" else "R"

    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if in_bounds(nx, ny):
            val = grid[ny][nx]
            if val == "#" or val == "3":
                rotate(grid, nx, ny, opposite, visited, outputs)
            elif val == "*" and direction == "L":
                grid[ny][nx] = "0"
            elif (val == "*" or val == "0") and direction == "R":
                grid[ny][nx] = "1"
            elif len(outputs) and 'a' <= val <= 'z':
                ox, oy = outputs[val.upper()]
                rotate(grid, ox, oy, direction, visited, outputs)

def get_num(grid):
    digits = []
    for y in range(0, height):
        for x in range(0, width):
            if grid[y][x] == "0" or grid[y][x] == "1":
                digits.append(grid[y][x])

    return int("".join(digits), 2)

def find_outputs(grid):
    outputs = {}
    for y in range(0, height):
        for x in range(0, width):
            if 'A' <= grid[y][x] <= 'Z':
                outputs[grid[y][x]] = (x, y)
    return outputs


dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

orig_grid = []
for line in open('input.txt').read().splitlines():
    orig_grid.append(list(line))
height = len(orig_grid)
width = len(orig_grid[0])
start_x, start_y = find_start(orig_grid)

grid = clone(orig_grid)
visited = set()
rotate(grid, start_x, start_y, "L", visited, {})
print(get_num(grid))

grid = clone(orig_grid)
outputs = find_outputs(grid)
visited = set()
rotate(grid, start_x, start_y, "L", visited, outputs)
print(get_num(grid))
