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
        self.sprouts = { self.start : '00' }
        self.stems = set()
        self.max_height = 1

    def add_sprout(self, sprouts, loc, id, other_trees):
        if id == 'XX':
            return False
        if loc in self.stems:
            return False
        if loc in sprouts and int(sprouts[loc]) > int(id):
            return False
        for tree in other_trees:
            if loc in tree.stems or loc in tree.sprouts:
                return False
        sprouts[loc] = id
        return True

    def grow(self, other_trees):
        new_sprouts = {}

        for loc, id in self.sprouts.items():
            x, y = loc

            self.stems.add(loc)

            dna = self.configuration[id]

            self.add_sprout(new_sprouts, (x - 1, y), dna.left, other_trees)
            self.add_sprout(new_sprouts, (x + 1, y), dna.right, other_trees)
            if self.add_sprout(new_sprouts, (x, y + 1), dna.top, other_trees):
                self.max_height = max(self.max_height, y + 1)

        self.sprouts = new_sprouts
        self.age += 1

    def energy_check(self, other_trees, other_max_height):
        if self.age < 5:
            return True

        if self.age == 100:
            self.alive = False
            return False

        scan_height = max(self.max_height, other_max_height)

        energy_produced = 0 
        for loc in self.stems:
            x, y = loc

            height = y

            if height > 10:
                height = 10

            multiplier = 3

            for ny in range(y + 1, scan_height + 1):
                above = (x, ny)
                stem = False

                if above in self.stems:
                    stem = True

                if stem == False:
                    for tree in other_trees:
                        if above in tree.stems:
                            stem = True
                            break

                if stem:
                    multiplier -= 1
                    if multiplier == 0:
                        break

            energy_produced += height * multiplier

        energy_needed = (len(self.stems) + len(self.sprouts)) * 3
        if energy_produced < energy_needed:
            self.alive = False
            return False
        else:
            return True

    def mass(self):
        return len(self.stems) + len(self.sprouts)


data = open('input.txt').read().splitlines()
#data = open('example2.txt').read().splitlines()

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
        tree.grow([])
        if not tree.energy_check({}, 0):
            break

    total_mass += tree.mass()

print(total_mass)


max_height = 200

x = 0
for tree in trees:
    tree.start = (x, 1)
    tree.reset()
    x += 10

while any(tree.alive for tree in trees):
    for tree in trees:
        if tree.alive:
            tree.grow(trees)

    for tree in trees:
        if tree.alive:
            tree.energy_check(trees, max_height)

total_mass = 0
for tree in trees:
    total_mass += tree.mass()

print(total_mass)
