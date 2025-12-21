#!/usr/bin/python3
import copy
import functools

f = open('input.txt')
lines = f.read().splitlines()

@functools.cache
def path_count(x, y):
    if x < 0 or y < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    return path_count(x-1, y) + path_count(x, y-1)

@functools.cache
def path_count_multi(dimensions):
    if any(val < 0 for val in dimensions):
        return 0
    if all(val == 0 for val in dimensions):
        return 1

    total = 0
    for i in range(len(dimensions)):
        d_copy = list(dimensions)
        d_copy[i] -= 1
        total += path_count_multi(tuple(d_copy))
    return total

part1, part2, part3 = 0, 0, 0
for line in lines:
    x, y = [int(n) for n in line.split()]
    part1 += path_count(x-1, y-1)

    dimensions = (x-1, y-1, x-1)
    part2 += path_count_multi(dimensions)

    dimensions = []
    for _ in range(x):
        dimensions.append(y-1)
    part3 += path_count_multi(tuple(dimensions))

print(f"{part1}\n{part2}\n{part3}")
