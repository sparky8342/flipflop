#!/usr/bin/python3
from sympy import isprime

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
                output = val.upper()
                if output in outputs:
                    ox, oy = outputs[output]
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

def remove_prime_outputs(outputs):
    to_delete = []

    for output, location in outputs.items():
        queue = [location]
        visited = set()
        visited.add(location)

        while(len(queue) > 0):
            loc = queue.pop(0)
            x, y = loc

            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]
                if in_bounds(nx, ny) and grid[ny][nx] == "3":
                    new_loc = (nx, ny)
                    if new_loc in visited:
                        continue
                    queue.append(new_loc)
                    visited.add(new_loc)

        group = len(visited) - 1
        if isprime(group):
            to_delete.append(output)

    for name in to_delete:
        del(outputs[name])

def find_number(grid, start_x, start_y, outputs):
    cl = clone(grid)
    rotate(cl, start_x, start_y, "L", set(), outputs)
    return get_num(cl)


dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

grid = []
for line in open('input.txt').read().splitlines():
    grid.append(list(line))
height = len(grid)
width = len(grid[0])
start_x, start_y = find_start(grid)
outputs = find_outputs(grid)

part1 = find_number(grid, start_x, start_y, {})
part2 = find_number(grid, start_x, start_y, outputs)
remove_prime_outputs(outputs)
part3 = find_number(grid, start_x, start_y, outputs)

print(f"{part1}\n{part2}\n{part3}")
