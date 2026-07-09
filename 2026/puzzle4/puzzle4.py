#!/usr/bin/python3

flower = open('input.txt').read().splitlines()

cut = len(flower) - 400 - 1

leaves = 0
for i in range(cut, 3, -1):
    if flower[i][0] == 'o' or (len(flower[i]) == 5 and flower[i][4] == 'o'):
        leaves += 1

print(leaves)

swaps = 0
last_side = ""
for i in range(len(flower) - 2, 2, -1):
    side = ""
    if flower[i][0] == 'o':
        side = "L"
    elif len(flower[i]) == 5 and flower[i][4] == 'o':
        side = "R"
    else:
        continue

    if last_side == "":
        last_side = side
    elif last_side != side:
        swaps += 1
        last_side = side

print(swaps)
