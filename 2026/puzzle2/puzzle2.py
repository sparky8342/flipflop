#!/usr/bin/python3

WALL_SIZE = 100

moves = list(open('input.txt').read().strip())

wall = [0] * WALL_SIZE
pos = 0

for move in moves:
    if move == '<':
        pos -= 1
    elif move == '>':
        pos += 1
    pos %= WALL_SIZE
    wall[pos] += 1

max_heat = wall[0]
max_pos = 0

for i, heat in enumerate(wall):
    if heat > max_heat:
        max_heat = heat
        max_pos = i

print((max_pos + 1) * max_heat)
