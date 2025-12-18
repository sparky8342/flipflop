#!/usr/bin/python3

class Bird:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

def take_pictures(birds, seconds, repeats):
    for bird in birds:
        bird.x = 0
        bird.y = 0

    count = 0
    for _ in range(repeats):
        for bird in birds:
            bird.x = (bird.x + bird.vx * seconds) % size
            bird.y = (bird.y + bird.vy * seconds) % size

            if start <= bird.x < end and start <= bird.y < end:
                count += 1
    return count

size = 1000
start = size // 4
end = start * 3

f = open('input.txt')
lines = f.read().splitlines()

birds = []
for line in lines:
    vx, vy = line.split(",")
    birds.append(Bird(0, 0, int(vx), int(vy)))

print(take_pictures(birds, 100, 1))
print(take_pictures(birds, 3600, 1000))
print(take_pictures(birds, 31556926, 1000))
