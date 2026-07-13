#!/usr/bin/python3
from collections import defaultdict

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

print(sum(stoats.values()))

rules = {}
for line in lines:
    rule = line.split(" ")
    rules[rule[0] + rule[1]] = rule[2:]
    rules[rule[1] + rule[0]] = rule[2:]

stoats = ["A", "B"]

for _ in range(0, 7):
    new_stoats = [stoats[0]]
    for i in range(0, len(stoats) - 1):
        pair = stoats[i] + stoats[i+1]
        if pair in rules:
            new_stoats.extend(rules[pair])
            new_stoats.append(stoats[i+1])
    stoats = new_stoats

print(len(stoats))
