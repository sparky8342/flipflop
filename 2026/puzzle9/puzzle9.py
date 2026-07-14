#!/usr/bin/python3
from collections import deque

def find_start_end(grid):
    for y in range(0, size):
        for x in range(0, size):
            if grid[y][x] == "S":
                start = (x, y)
            elif grid[y][x] == "E":
                end = (x, y)
    return start, end

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
grid = open('input.txt').read().splitlines()
size = len(grid)

start, end = find_start_end(grid)

part1 = 0
queue = deque()
queue.append((start[0], start[1], 0))
visited = set()
visited.add(start)

while(len(queue) > 0):
    entry = queue.popleft()
    x, y, distance = entry[0], entry[1], entry[2]

    if x == end[0] and y == end[1]:
        part1 = distance
        break

    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if grid[ny][nx] != "#":
            new_loc = (nx, ny)
            if new_loc in visited:
                continue
            queue.append((nx, ny, distance + 1))
            visited.add(new_loc)

print(part1)
