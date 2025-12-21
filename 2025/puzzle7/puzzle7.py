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
def path_count3d(x, y, z):
    if x < 0 or y < 0 or z < 0:
        return 0
    if x == 0 and y == 0 and z == 0:
        return 1
    return path_count3d(x-1, y, z) + path_count3d(x, y-1, z) + path_count3d(x, y, z-1)

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

total = 0
for line in lines:
    width, height = line.split()
    total += path_count(int(width)-1, int(height)-1)
print(total)

total = 0
for line in lines:
    width, height = line.split()
    total += path_count3d(int(width)-1, int(height)-1, int(width)-1)
print(total)

total = 0
for line in lines:
    amount, size = line.split()
    dimensions = []
    for _ in range(0, int(amount)):
        dimensions.append(int(size)-1)
    total += path_count_multi(tuple(dimensions))
print(total)
