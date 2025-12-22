#!/usr/bin/python3
import copy
import functools

f = open('input.txt')
lines = f.read().splitlines()

@functools.cache
def path_count(dimensions):
    if all(val == 0 for val in dimensions):
        return 1

    total = 0
    for i in range(len(dimensions)):
        if dimensions[i] > 0:
            d_copy = list(dimensions)
            d_copy[i] -= 1
            total += path_count(tuple(d_copy))
    return total

part1, part2, part3 = 0, 0, 0
for line in lines:
    x, y = [int(n) for n in line.split()]

    dimensions = (x-1, y-1)
    part1 += path_count(dimensions)

    dimensions = (x-1, y-1, x-1)
    part2 += path_count(dimensions)

    dimensions = []
    for _ in range(x):
        dimensions.append(y-1)
    part3 += path_count(tuple(dimensions))

print(f"{part1}\n{part2}\n{part3}")
