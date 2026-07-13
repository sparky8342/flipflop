#!/usr/bin/python3
from collections import defaultdict
from functools import cache

lines = open('input.txt').read().splitlines()

rules = {}
for line in lines:
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

part1 = sum(stoats.values())

rules = {}
for line in lines:
    rule = line.split(" ")
    rules[rule[0] + rule[1]] = rule[2:]
    rules[rule[1] + rule[0]] = rule[2:]

@cache
def get_count(pair, generation):
    if generation == 0:
        return 2

    count = 0
    new_group = [pair[0]]
    new_group.extend(rules[pair])
    new_group.append(pair[1])
    for i in range(0, len(new_group) - 1):
        count += get_count(new_group[i] + new_group[i+1], generation - 1)
    count -= len(new_group) - 2

    return count

part2 = get_count("AB", 7)
part3 = get_count("AB", 21)

print(f"{part1}\n{part2}\n{part3}")
