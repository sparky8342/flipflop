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

def distinct_streets_with_turns(grid):
    turns = 0
    x, y = 0, 0
    visited = set()
    visited.add((0, 0))

    illegal_turn = False
    while True:
        if illegal_turn:
            match grid[y][x]:
                case 'v':
                    x -= 1
                case '<':
                    y -= 1
                case '^':
                    x += 1
                case '>':
                    y += 1
            illegal_turn = False
        else:
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
            if turns == 3 or y == 0 or y == size - 1 or x == 0 or x == size - 1:
                return len(visited)

            illegal_turn = True
            turns += 1
            continue
        visited.add(loc)

def find_best_change(grid, find_path):
    max_amount = 0

    for y in range(1, size - 1):
        for x in range(1, size - 1):

            val = grid[y][x]
            for direction in ['v', '<', '^', '>']:
                if val == direction:
                    continue
                grid[y][x] = direction
                amount = find_path(grid)
                max_amount = max(amount, max_amount)

            grid[y][x] = val

    return max_amount


grid = []
for line in open('input.txt').read().splitlines():
    grid.append(list(line))
size = len(grid)

part1 = distinct_streets(grid)
part2 = find_best_change(grid, distinct_streets)
part3 = find_best_change(grid, distinct_streets_with_turns)

print(f"{part1}\n{part2}\n{part3}")
