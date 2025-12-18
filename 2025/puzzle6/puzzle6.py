#!/usr/bin/python3

class Bird:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

f = open('input.txt')
#f = open('test.txt')
lines = f.read().splitlines()

size = 1000
#size = 8
seconds = 100
start = size // 4
end = start * 3

print(size, start, end)

birds = []
for line in lines:
    vx, vy = line.split(",")
    birds.append(Bird(0, 0, int(vx), int(vy)))

for bird in birds:
    bird.x = (bird.x + bird.vx * seconds) % size
    bird.y = (bird.y + bird.vy * seconds) % size
        
count = 0
for bird in birds:
    if start <= bird.x < end and start <= bird.y < end:
        count += 1

print(count)


birds = []
for line in lines:
    vx, vy = line.split(",")
    birds.append(Bird(0, 0, int(vx), int(vy)))

count = 0
for _ in range(1000):
    for bird in birds:
        bird.x = (bird.x + bird.vx * 3600) % size
        bird.y = (bird.y + bird.vy * 3600) % size

    for bird in birds:
        if start <= bird.x < end and start <= bird.y < end:
            count += 1

print(count)


birds = []
for line in lines:
    vx, vy = line.split(",")
    birds.append(Bird(0, 0, int(vx), int(vy)))

count = 0
for _ in range(1000):
    for bird in birds:
        bird.x = (bird.x + bird.vx * 31556926) % size
        bird.y = (bird.y + bird.vy * 31556926) % size

    for bird in birds:
        if start <= bird.x < end and start <= bird.y < end:
            count += 1

print(count)
