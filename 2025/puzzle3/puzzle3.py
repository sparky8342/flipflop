#!/usr/bin/python3
from collections import defaultdict

f = open('input.txt')
lines = f.read().splitlines()

colours = defaultdict(int)
red = 0
green = 0
blue = 0
special = 0
for line in lines:
    colours[line] += 1
    r, g, b = [int(x) for x in line.split(",")]
    if r == g or r == b or g == b:
        special += 1
    elif r > g and r > b:
        red += 1
    elif g > r and g > b:
        green += 1
    elif b > r and b > g:
        blue += 1

colours_s = sorted(colours.keys(), key=lambda x : colours[x], reverse=True)
print(colours_s[0])
print(green)
print(red*5+green*2+blue*4+special*10)
