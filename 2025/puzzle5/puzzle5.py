#!/usr/bin/python3
from collections import defaultdict

class Info:
    def __init__(self, name, destination, distance):
        self.name = name
        self.destination = destination
        self.distance = distance

f = open('input.txt')
line = f.read().strip()

letters = defaultdict(list)
for i, char in enumerate(line):
    letters[char].append(i)

lookup = {}
for name, locations in letters.items():
    start, end = locations
    distance = end - start
    lookup[start] = Info(name, end, distance)
    lookup[end] = Info(name, start, distance)

pos = 0
distance = 0
power_distance = 0
visited = set()
while pos < len(line):
    info = lookup[pos]
    visited.add(info.name)
    distance += info.distance
    if info.name.isupper():
        power_distance -= info.distance
    else:
        power_distance += info.distance
    pos = info.destination + 1

not_visited = []
for char in line:
    if char not in visited:
        not_visited.append(char)
        visited.add(char)

print(distance)
print("".join(not_visited))
print(power_distance)
