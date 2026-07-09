#!/usr/bin/python3

flower = open('input.txt').read().splitlines()

leaves = []
for i in range(len(flower)-2, 2, -1):
    if flower[i][0] == 'o':
        leaves.append("L")
    elif len(flower[i]) == 5 and flower[i][4] == 'o':
        leaves.append("R")
    else:
        leaves.append("")

part1 = 0
for i in range(400, len(leaves)):
    if leaves[i] != "":
        part1 += 1

leaves = [x for x in leaves if x != ""]

part2 = 0
side = leaves[0]
for leaf in leaves:
    if side != leaf:
        part2 += 1
        side = leaf

part3 = 0
while True:
    side = leaves[0]
    for i, leaf in enumerate(leaves):
        if side != leaf:
            leaves[i] = ""
            side = leaf

    part3 += 1

    leaves[0] = ""
    leaves = [x for x in leaves if x != ""]
    if len(leaves) == 0:
        break

print(f"{part1}\n{part2}\n{part3}")
