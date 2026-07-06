#!/usr/bin/python3

time = 0

f = open('input.txt')
for line in f.read().splitlines():
    t = int(line)
    if t < 60:
        time += 60 - t

print(time)
