#!/usr/bin/python3

lines = open('input.txt').read().splitlines()
directions = lines[0]
sushi = []
for i in range(2, len(lines)):
    x, y = lines[i].split(",")
    sushi.append((int(x), int(y)))

x, y = 0, 0
sushi_i = 0
sushi_x, sushi_y = sushi[sushi_i]
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
        sushi_i += 1
        sushi_x, sushi_y = sushi[sushi_i]

part1 = eaten

snake = [(0, 0)]
sushi_i = 0
sushi_x, sushi_y = sushi[sushi_i]
x, y = 0, 0
for direction in directions:
    match direction:
        case '^':
            y += 1
        case '>':
            x += 1
        case 'v':
            y -= 1
        case '<':
            x -= 1
    if sushi_x == x and sushi_y == y:
        sushi_i += 1
        sushi_x, sushi_y = sushi[sushi_i]
        snake.append((x, y))
    else:
        snake.pop(0)
        if (x, y) in snake:
            break
        snake.append((x, y))

part2 = len(snake) + 1

snake = [(0, 0)]
sushi_i = 0
sushi_x, sushi_y = sushi[sushi_i]
x, y = 0, 0
bites = 0
for direction in directions:
    match direction:
        case '^':
            y += 1
        case '>':
            x += 1
        case 'v':
            y -= 1
        case '<':
            x -= 1
    if sushi_x == x and sushi_y == y:
        sushi_i += 1
        if sushi_i == len(sushi):
            sushi_x, sushi_y = -1, -1
        else:
            sushi_x, sushi_y = sushi[sushi_i]
        snake.append((x, y))
    else:
        snake.pop(0)
        if (x, y) in snake:
            pos = snake.index((x, y))
            snake = snake[pos+2:]
            bites += 1
        snake.append((x, y))

part3 = len(snake) * bites

print(f"{part1}\n{part2}\n{part3}")
