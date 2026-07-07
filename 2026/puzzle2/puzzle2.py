#!/usr/bin/python3

WALL_SIZE = 100

moves = list(open('input.txt').read().strip())

wall = [0] * WALL_SIZE
robot = 0

for move in moves:
    if move == '<':
        robot -= 1
    elif move == '>':
        robot += 1
    robot %= WALL_SIZE
    wall[robot] += 1

max_heat = wall[0]
max_robot = 0

for i, heat in enumerate(wall):
    if heat > max_heat:
        max_heat = heat
        max_robot = i

part1 = (max_robot + 1) * max_heat

robot = 0
wall_segment = 0
part2 = 0
rev_moves = list(reversed(moves))

for i in range(0, len(moves)):
    if moves[i] == '<':
        robot -= 1
    elif moves[i] == '>':
        robot += 1
    robot %= WALL_SIZE

    if rev_moves[i] == '<':
        wall_segment -= 1
    elif rev_moves[i] == '>':
        wall_segment += 1
    wall_segment %= WALL_SIZE

    if robot == wall_segment:
       part2 += 1

print(f"{part1}\n{part2}")
