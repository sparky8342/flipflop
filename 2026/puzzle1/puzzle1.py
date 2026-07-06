#!/usr/bin/python3

part1, part2 = 0, 0

temps = [int(x) for x in open('input.txt').read().splitlines()]

for temp in temps:
    if temp < 60:
        part1 += 60 - temp
    elif temp > 60:
        part2 += (temp - 60) * 5

part2 += part1

part3 = 0
amount = len(temps) // 2
for i in range(0, amount):
    temp = temps[i]
    desired = temps[i+amount]
    if desired < temp:
        part3 += (temp - desired) * 5
    elif desired > temp:
        part3 += desired - temp

print(f"{part1}\n{part2}\n{part3}")
