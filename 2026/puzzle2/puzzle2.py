#!/usr/bin/python3

WALL_SIZE = 100

def move_robot(robot, move):
    if move == '<':
        robot -= 1
    elif move == '>':
        robot += 1
    robot %= WALL_SIZE
    return robot

def max_heat(wall):
    max_h = wall[0]
    max_robot = 0

    for i, heat in enumerate(wall):
        if heat > max_h:
            max_h = heat
            max_robot = i

    return max_h, max_robot


moves = list(open('input.txt').read().strip())

wall = [0] * WALL_SIZE
robot = 0

for move in moves:
    robot = move_robot(robot, move)
    wall[robot] += 1

heat, robot = max_heat(wall)
part1 = (robot + 1) * heat

robot = 0
wall_segment = 0
part2 = 0
rev_moves = list(reversed(moves))

for i in range(0, len(moves)):
    robot = move_robot(robot, moves[i])
    wall_segment = move_robot(wall_segment, rev_moves[i])

    if robot == wall_segment:
       part2 += 1

wall = [0] * WALL_SIZE
wall_shift = 0

for i in range(0, len(moves)):
    robot = move_robot(robot, moves[i])

    if rev_moves[i] == '<':
        wall_shift += 1
    elif rev_moves[i] == '>':
        wall_shift -= 1

    wall[(robot + wall_shift) % WALL_SIZE] += 1

heat, robot = max_heat(wall)
part3 = ((robot + wall_shift) % WALL_SIZE + 1) * heat

print(f"{part1}\n{part2}\n{part3}")
