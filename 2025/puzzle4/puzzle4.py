#!/usr/bin/python3

f = open('input.txt')
lines = f.read().splitlines()

distance = 0
x, y = 0, 0
for line in lines:
    tx, ty = [int(x) for x in line.split(",")]
    distance += abs(tx - x) + abs(ty - y)
    x, y = tx, ty

print(distance)
