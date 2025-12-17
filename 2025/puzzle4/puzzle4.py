#!/usr/bin/python3

def diag_distance(trash):
    distance = 0
    x, y = 0, 0
    for tx, ty in trash:
        x_dist = abs(tx - x)
        y_dist = abs(ty - y)

        if x_dist == y_dist:
            distance += x_dist
        elif x_dist < y_dist:
            distance += x_dist + (y_dist - x_dist)
        elif y_dist < x_dist:
            distance += y_dist + (x_dist - y_dist)

        x, y = tx, ty
    return distance

f = open('input.txt')
lines = f.read().splitlines()

trash = []
for line in lines:
    x, y = [int(n) for n in line.split(",")]
    trash.append((x, y))

distance = 0
x, y = 0, 0
for tx, ty in trash:
    distance += abs(tx - x) + abs(ty - y)
    x, y = tx, ty
print(distance)

print(diag_distance(trash))
trash = sorted(trash, key=lambda n : n[0] + n[1])
print(diag_distance(trash))
