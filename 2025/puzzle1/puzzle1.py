#!/usr/bin/python3

part1, part2, part3 = 0, 0, 0

f = open('input.txt')
for line in f.read().splitlines():
    l = len(line) // 2
    part1 += l
    if l % 2 == 0:
        part2 += l
    if "e" not in line:
        part3 += l

print(f"{part1}\n{part2}\n{part3}")
