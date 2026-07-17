#!/usr/bin/python3

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
                global max_height
                max_height = max(max_height, y + 1)

        self.sprouts = new_sprouts
        self.age += 1

    def energy_check(self, other_trees):
        if self.age < 5:
            return True

        if self.age == 100:
            self.alive = False
            return False

        energy_produced = 0 
        for loc in self.stems:
            x, y = loc

            height = y

            if height > 10:
                height = 10

            multiplier = 3

            for ny in range(y + 1, max_height + 1):
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

    def next_generation(self):
        new_trees = []
        for loc in self.sprouts.keys():
            tree = Tree(-1, self.configuration)
            tree.start = loc
            new_trees.append(tree)
        return new_trees


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

max_height = 1

total_mass = 0
for tree in trees:
    while True:
        tree.grow([])
        if not tree.energy_check({}):
            break

    total_mass += tree.mass()

print(total_mass)


def run_sim(trees):
    while any(tree.alive for tree in trees):
        for tree in trees:
            if tree.alive:
                tree.grow(trees)

        for tree in trees:
            if tree.alive:
                tree.energy_check(trees)

max_height = 1
x = 0
for tree in trees:
    tree.start = (x, 1)
    tree.reset()
    x += 10

run_sim(trees)

total_mass = 0
for tree in trees:
    total_mass += tree.mass()

print(total_mass)

for _ in range(0, 2):
    new_trees = []
    for tree in trees:
        new_trees += tree.next_generation()

    new_trees = sorted(new_trees, key=lambda t : (t.start[0], -t.start[1]))
    pos = 0
    while pos < len(new_trees) - 1:
        if new_trees[pos].start[0] == new_trees[pos+1].start[0]:
            new_trees.pop(pos+1)
        else:
            pos += 1

    for i in range(0, len(new_trees)):
        new_trees[i].id = i
        new_trees[i].start = (new_trees[i].start[0], 1)
        new_trees[i].reset()

    trees = new_trees
    max_height = 1
    run_sim(trees)

total_mass = 0
for tree in trees:
    total_mass += tree.mass()

print(total_mass)
