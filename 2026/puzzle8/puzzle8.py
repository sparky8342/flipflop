#!/usr/bin/python3
from collections import defaultdict

rules = {}
for line in open('input.txt').read().splitlines():
    rule = line.split(" ")
    group = rule[0]
    if group not in rules:
        rules[group] = rule[1:]

stoats = { "A" : 1, "B" : 1 }

for _ in range(0, 7):
    new_stoats = defaultdict(int)
    for group, amount in stoats.items():
        for new_group in rules[group]:
            new_stoats[new_group] += amount
    stoats = new_stoats

print(sum(stoats.values()))
