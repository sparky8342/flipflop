#!/usr/bin/python3
from collections import defaultdict

f = open('input.txt')
line = f.read().strip()

letters = defaultdict(list)
for i, char in enumerate(line):
    letters[char].append(i)

lookup = {}
for name, locations in letters.items():
    start, end = locations
    distance = end - start
    lookup[start] = (name, end, distance)
    lookup[end] = (name, start, distance)

p = 0
distance = 0
visited = set()
while p < len(line):
    info = lookup[p]
    visited.add(info[0])
    distance += info[2]
    p = info[1] + 1

not_visited = []
for char in line:
    if char not in visited:
        not_visited.append(char)
        visited.add(char)

print(distance)
print("".join(not_visited))
