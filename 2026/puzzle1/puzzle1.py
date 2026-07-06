#!/usr/bin/python3

p1, p2 = 0, 0

f = open('input.txt')
for line in f.read().splitlines():
    t = int(line)
    if t < 60:
        p1 += 60 - t
    elif t > 60:
        p2 += (t - 60) * 5

p2 += p1

print(p1, p2)
