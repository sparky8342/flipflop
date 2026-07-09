#!/usr/bin/python3

flower = open('input.txt').read().splitlines()

cut = len(flower) - 400 - 1

leaves = 0
for i in range(cut, 3, -1):
    if flower[i][0] == 'o' or (len(flower[i]) == 5 and flower[i][4] == 'o'):
        leaves += 1

print(leaves)
