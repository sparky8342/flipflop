#!/usr/bin/python3
from collections import deque
import heapq

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
    x, y, distance = queue.popleft()

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


part2 = 0
queue = [(0, start[0], start[1])]
visited = {}
visited[start] = 0

while(len(queue) > 0):
    distance, x, y = heapq.heappop(queue)

    if x == end[0] and y == end[1]:
        part2 = distance
        break

    new_distance = distance + 1
    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if grid[ny][nx] != "#":
            new_loc = (nx, ny)
            if new_loc not in visited or visited[new_loc] > new_distance:
                heapq.heappush(queue, (new_distance, nx, ny))
                visited[new_loc] = new_distance

            if grid[ny + dir[1]][nx + dir[0]] == "#":
                continue

            while grid[ny + dir[1]][nx + dir[0]] != "#":
                nx += dir[0]
                ny += dir[1]

            new_loc = (nx, ny)
            if new_loc not in visited or visited[new_loc] > new_distance:
                heapq.heappush(queue, (new_distance, nx, ny))
                visited[new_loc] = new_distance


part3 = 0
queue = [(0, start[0], start[1], False)]
visited = {}
visited[start] = 0

while(len(queue) > 0):
    distance, x, y, from_portal = heapq.heappop(queue)

    if x == end[0] and y == end[1]:
        part3 = distance
        break

    wall_neighbour = False
    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]
        if grid[ny][nx] == "#":
            wall_neighbour = True
        elif grid[ny][nx] != "#":
            new_loc = (nx, ny)
            if new_loc not in visited or visited[new_loc] > distance + 1:
                heapq.heappush(queue, (distance + 1, nx, ny, False))
                visited[new_loc] = distance + 1

    if wall_neighbour:
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]

            if grid[ny][nx] != "#":
                if grid[ny + dir[1]][nx + dir[0]] == "#":
                    continue

                while grid[ny + dir[1]][nx + dir[0]] != "#":
                    nx += dir[0]
                    ny += dir[1]

                new_loc = (nx, ny)
                new_distance = distance + 2
                if from_portal == False:
                    new_distance += 1
                if new_loc not in visited or visited[new_loc] > new_distance:
                    heapq.heappush(queue, (new_distance, nx, ny, True))
                    visited[new_loc] = new_distance


print(f"{part1}\n{part2}\n{part3}")
