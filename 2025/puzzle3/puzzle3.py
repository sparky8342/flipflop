#!/usr/bin/python3
from collections import defaultdict

f = open('input.txt')
lines = f.read().splitlines()

colours = defaultdict(int)
for line in lines:
    colours[line] += 1
colours_s = sorted(colours.keys(), key=lambda x : colours[x], reverse=True)
print(colours_s[0])

green = 0
for line in lines:
    r, g, b = [int(x) for x in line.split(",")]
    if g > r and g > b and r != g and r != b and g != b:
        green += 1
print(green)
