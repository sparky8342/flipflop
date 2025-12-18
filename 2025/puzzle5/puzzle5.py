#!/usr/bin/python3
from collections import defaultdict

f = open('input.txt')
line = f.read().strip()

letters = defaultdict(list)
for i, char in enumerate(line):
    letters[char].append(i)

lookup = {}
for a, b in letters.values():
    lookup[a] = b
    lookup[b] = a

p = 0
distance = 0
while p < len(line):
    new_p = lookup[p]
    distance += abs(new_p - p)
    p = new_p + 1

print(distance)
