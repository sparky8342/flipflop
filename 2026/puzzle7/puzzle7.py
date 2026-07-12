#!/usr/bin/python3

lines = open('input.txt').read().splitlines()
directions = lines[0]
sushi = []
for i in range(2, len(lines)):
    x, y = lines[i].split(",")
    sushi.append((int(x), int(y)))

x, y = 0, 0
sushi_x, sushi_y = sushi.pop(0)
eaten = 0
for i in range(0, len(directions) // 2):
    match directions[i]:
        case '^':
            y += 1
        case '>':
            x += 1
        case 'v':
            y -= 1
        case '<':
            x -= 1
    if sushi_x == x and sushi_y == y:
        eaten += 1
        sushi_x, sushi_y = sushi.pop(0)

print(eaten)
