#!/usr/bin/python3
import functools

@functools.cache
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

f = open('input.txt')
line = list(f.read())

highest = 0
height = 0
for c in line:
    if c == '^':
        height += 1
        highest = max(highest, height)
    elif c == 'v':
        height -= 1
print(highest)

highest = 0
height = 0
up = 1
down = 1
for c in line:
    if c == '^':
        height += up
        highest = max(highest, height)
        up += 1
        down = 1
    elif c == 'v':
        height -= down
        down += 1
        up = 1
print(highest)

highest = 0
height = 0
up = 0
down = 0
for c in line:
    if c == '^':
        if down > 0:
            height -= fib(down)
        up += 1
        down = 0
    elif c == 'v':
        if up > 0:
            height += fib(up)
            highest = max(highest, height)
        down += 1
        up = 0

if down > 0:
        height -= fib(down)
elif up > 0:
        height += fib(down)
        highest = max(highest, height)

print(highest)
