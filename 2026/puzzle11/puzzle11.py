#!/usr/bin/python3
import copy

class DNA:
    def __init__(self, id, left, top, right):
        self.id = id
        self.left = left
        self.top = top
        self.right = right

class Part:
    def __init__(self, id, tree_id):
        self.id = id
        self.tree_id = tree_id

class Tree:
    def __init__(self, id, configuration):
        self.id = id
        self.configuration = configuration
        self.start = (0, 1)
        self.reset()

    def reset(self):
        self.age = 0
        self.alive = True
        self.parts = { self.start : Part('00', self.id) }
        self.max_height = 1

    def add_sprout(self, parts, loc, id):
        if id == 'XX':
            return False
        if loc in parts and (parts[loc].id == '#' or int(parts[loc].id) > int(id)):
            return False
        parts[loc] = Part(id, self.id)
        return True

    def grow(self):
        new_parts = copy.deepcopy(self.parts)

        for loc, part in self.parts.items():
            x, y = loc

            if part.id != '#':
                new_parts[loc].id = '#'
                dna = self.configuration[part.id]

                self.add_sprout(new_parts, (x - 1, y), dna.left)
                self.add_sprout(new_parts, (x + 1, y), dna.right)
                if self.add_sprout(new_parts, (x, y + 1), dna.top):
                    self.max_height = max(self.max_height, y + 1)

        self.parts = new_parts
        self.age += 1

    def energy_check(self, other_parts, other_max_height):
        if self.age < 5:
            return True

        if self.age == 100:
            self.alive = False
            return False

        scan_height = max(self.max_height, other_max_height)

        energy_produced = 0 
        for loc, part in self.parts.items():
            x, y = loc

            if part.id == '#':
                height = y

                if height > 10:
                    height = 10

                multiplier = 3

                for ny in range(y + 1, scan_height + 1):
                    above = (x, ny)
                    if (above in self.parts and self.parts[above].id == '#') or (above in other_parts and other_parts[above].id == '#'):
                        multiplier -= 1
                        if multiplier == 0:
                            break

                energy_produced += height * multiplier

        energy_needed = len(self.parts) * 3
        if energy_produced < energy_needed:
            self.alive = False
            return False
        else:
            return True

    def mass(self):
        return len(self.parts)


data = open('input.txt').read().splitlines()

trees = []
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

    tree = Tree(len(trees), configuration)
    trees.append(tree)

total_mass = 0
for tree in trees:
    while True:
        tree.grow()
        if not tree.energy_check({}, 0):
            break

    total_mass += tree.mass()

print(total_mass)


max_height = 0
global_parts = {}

x = 0
for tree in trees:
    tree.start = (x, 1)
    tree.reset()
    x += 10

while any(tree.alive for tree in trees):
    for tree in trees:
        if tree.alive:
            tree.grow()

            to_delete = []
            for loc, part in tree.parts.items():
                if loc in global_parts:
                    if tree.id != global_parts[loc].tree_id:
                        to_delete.append(loc)
                        continue
                    elif global_parts[loc].id == part.id:
                        continue

                global_parts[loc] = part
                max_height = max(max_height, loc[1])

            for loc in to_delete:
                del(tree.parts[loc])

    for tree in trees:
        if tree.alive:
            tree.energy_check(global_parts, max_height)

total_mass = 0
for tree in trees:
    total_mass += tree.mass()

print(total_mass)
