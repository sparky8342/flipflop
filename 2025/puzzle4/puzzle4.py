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

distance = 0
x, y = 0, 0
for line in lines:
    tx, ty = [int(x) for x in line.split(",")]

    x_dist = abs(tx - x)
    y_dist = abs(ty - y)

    if x_dist == y_dist:
        distance += x_dist
        x_dist, y_dist = 0, 0
    elif x_dist < y_dist:
        distance += x_dist + (y_dist - x_dist)
    elif y_dist < x_dist:
        distance += y_dist + (x_dist - y_dist)

    x, y = tx, ty

print(distance)
