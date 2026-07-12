#!/usr/bin/python3
from collections import deque
from sympy import isprime

class Machine:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.find_start()
        self.outputs = {}
        self.digit_grid = []

    def reset_digit_grid(self):
        self.digit_grid = []
        for i in range(0, self.height):
            self.digit_grid.append([""] * self.width)

    def find_start(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if grid[y][x] == 'S':
                    self.start = (x, y)

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def rotate(self, x, y, direction, visited):
        pos = (x, y)
        if pos in visited:
            return
        visited.add(pos)

        opposite = "L" if direction == "R" else "R"

        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if self.in_bounds(nx, ny):
                val = self.grid[ny][nx]
                if val == "#" or val == "3":
                    self.rotate(nx, ny, opposite, visited)
                elif val == "*" and direction == "L":
                    self.digit_grid[ny][nx] = "0"
                elif (val == "*" or self.digit_grid[ny][nx] == "0") and direction == "R":
                    self.digit_grid[ny][nx] = "1"
                elif len(self.outputs) and 'a' <= val <= 'z':
                    output = val.upper()
                    if output in self.outputs:
                        ox, oy = self.outputs[output]
                        self.rotate(ox, oy, direction, visited)

    def get_num(self):
        digits = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.digit_grid[y][x] == "0" or self.digit_grid[y][x] == "1":
                    digits.append(self.digit_grid[y][x])

        return int("".join(digits), 2)

    def find_outputs(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if 'A' <= self.grid[y][x] <= 'Z':
                    self.outputs[self.grid[y][x]] = (x, y)

    def remove_prime_outputs(self):
        to_delete = []

        for output, location in self.outputs.items():
            queue = deque([location])
            visited = set()
            visited.add(location)

            while(len(queue) > 0):
                loc = queue.popleft()
                x, y = loc

                for dir in dirs:
                    nx = x + dir[0]
                    ny = y + dir[1]
                    if self.in_bounds(nx, ny) and self.grid[ny][nx] == "3":
                        new_loc = (nx, ny)
                        if new_loc in visited:
                            continue
                        queue.append(new_loc)
                        visited.add(new_loc)

            group = len(visited) - 1
            if isprime(group):
                to_delete.append(output)

        for name in to_delete:
            del(self.outputs[name])

    def find_number(self):
        self.reset_digit_grid()
        self.rotate(self.start[0], self.start[1], "L", set())
        return self.get_num()


dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

grid = []
for line in open('input.txt').read().splitlines():
    grid.append(list(line))

machine = Machine(grid)

part1 = machine.find_number()
machine.find_outputs()
part2 = machine.find_number()
machine.remove_prime_outputs()
part3 = machine.find_number()

print(f"{part1}\n{part2}\n{part3}")
