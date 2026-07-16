#!/usr/bin/python3
import copy

class DNA:
    def __init__(self, id, left, top, right):
        self.id = id
        self.left = left
        self.top = top
        self.right = right

class Tree:
    def __init__(self, configuration):
        self.configuration = configuration
        self.age = 0
        self.parts = { (0, 1) : '00' }
        self.max_height = 1

    def add_sprout(self, parts, loc, id):
        if id == 'XX':
            return False
        if loc in parts and (parts[loc] == '#' or int(parts[loc]) > int(id)):
            return False
        parts[loc] = id
        return True

    def grow(self):
        new_parts = copy.deepcopy(self.parts)

        for loc, id in self.parts.items():
            x, y = loc

            if id != '#':
                new_parts[loc] = '#'
                dna = configuration[id]

                self.add_sprout(new_parts, (x - 1, y), dna.left)
                self.add_sprout(new_parts, (x + 1, y), dna.right)
                if self.add_sprout(new_parts, (x, y + 1), dna.top):
                    self.max_height = max(self.max_height, y + 1)

        self.parts = new_parts
        self.age += 1

    def sufficient_energy(self):
        if self.age < 5:
            return True

        if self.age == 100:
            return False

        energy_produced = 0 
        for loc, id in self.parts.items():
            x, y = loc

            if id == '#':
                height = y

                if height > 10:
                    height = 10

                multiplier = 3

                for ny in range(y + 1, self.max_height + 1):
                    above = (x, ny)
                    if above in self.parts and self.parts[above] == '#':
                        multiplier -= 1
                        if multiplier == 0:
                            break

                energy_produced += height * multiplier

        energy_needed = len(self.parts) * 3
        return energy_produced >= energy_needed

    def mass(self):
        return len(self.parts)


data = open('input.txt').read().splitlines()

total_mass = 0
for i in range(0, len(data), 3):
    configuration = {}
    line1 = data[i].split()
    line2 = data[i + 1].split()

    top_i = 0
    for i in range(0, len(line2), 3):
        left = line2[i]
        id = line2[i+1]
        right = line2[i+2]
        top = line1[top_i]
        top_i += 1

        dna = DNA(id, left, top, right)
        configuration[id] = dna

    tree = Tree(configuration)

    while True:
        tree.grow()
        if not tree.sufficient_energy():
            break

    total_mass += tree.mass()

print(total_mass)
