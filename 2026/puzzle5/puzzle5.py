#!/usr/bin/python3

grid = open('input.txt').read().splitlines()

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
        break
    visited.add(loc)

print(len(visited))
