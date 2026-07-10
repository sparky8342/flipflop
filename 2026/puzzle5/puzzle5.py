#!/usr/bin/python3

def distinct_streets(grid):
    x, y = 0, 0
    visited = set()
    visited.add((0, 0))

    while True:
        match grid[y][x]:
            case 'v':
                y += 1
            case '<':
                x -= 1
            case '^':
                y -= 1
            case '>':
                x += 1

        loc = (x, y)
        if loc in visited:
            return len(visited)
        visited.add(loc)


grid = []
for line in open('input.txt').read().splitlines():
    grid.append(list(line))

print(distinct_streets(grid))

size = len(grid)
max_amount = 0

for y in range(1, size - 1):
    for x in range(1, size - 1):

        val = grid[y][x]
        for direction in ['v', '<', '^', '>']:
            if val == direction:
                continue
            grid[y][x] = direction
            amount = distinct_streets(grid)
            if amount > max_amount:
                max_amount = amount

        grid[y][x] = val

print(max_amount)
