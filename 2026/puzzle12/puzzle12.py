#!/usr/bin/python3

class Card:
    def __init__(self, nums):
        self.rows = []
        self.marks = []

        for i in range(0, 25, 5):
            self.rows.append(nums[i:i+5])
            self.marks.append([False, False, False, False, False])

        self.lookup = {}
        for y in range(0, 5):
            for x in range(0, 5):
                self.lookup[self.rows[y][x]] = (x, y)

        self.rows_completed = [False, False, False, False, False]
        self.columns_completed = [False, False, False, False, False]
        self.diagonals_completed = [False, False]
        self.bingos = 0

    def play_number(self, num):
        if num in self.lookup:
            x, y = self.lookup[num]
            self.marks[y][x] = True
            self.check_row(y)
            self.check_column(x)
            if x == y:
                self.check_diagonal1()
            if x + y == 4:
                self.check_diagonal2()
        return self.bingos

    def check_row(self, y):
        if self.rows_completed[y]:
            return
        for x in range(0, 5):
            if self.marks[y][x] == False:
                return
        self.rows_completed[y] = True
        self.bingos += 1
        
    def check_column(self, x):
        if self.columns_completed[x]:
            return
        for y in range(0, 5):
            if self.marks[y][x] == False:
                return
        self.columns_completed[x] = True
        self.bingos += 1
     
    def check_diagonal1(self):
        if self.diagonals_completed[0]:
            return
        x, y = 0, 0
        while x < 5 and y < 5:
            if self.marks[y][x] == False:
                return
            x += 1
            y += 1
        self.diagonals_completed[0] = True
        self.bingos += 1
     
    def check_diagonal2(self):
        if self.diagonals_completed[1]:
            return
        x, y = 0, 4
        while x < 5 and y >= 0:
            if self.marks[y][x] == False:
                return
            x += 1
            y -= 1
        self.diagonals_completed[1] = True
        self.bingos += 1
     

class Card3D:
    def __init__(self, nums):
        self.layers = []
        self.marks = []

        for i in range(0, 125, 25):
            rows = []
            mark = []
            for j in range(i, i + 25, 5):
                rows.append(nums[j:j + 5])
                mark.append([False, False, False, False, False])
            self.layers.append(rows)
            self.marks.append(mark)

    def play_number(self, num):
        for z in range(0, 5):
            for y in range(0, 5):
                for x in range(0, 5):
                    if self.layers[z][y][x] == num:
                        self.marks[z][y][x] = True
                        return

    def bingos(self):
        lines = set()
        for ordering in [[0, 1, 2], [1, 0, 2], [2, 0, 1]]:
            lines |= self.score(ordering)
        return len(lines)

    def score(self, ordering):
        score = 0

        lines = set()

        for val1 in range(0, 5):
            for val2 in range (0, 5):
                line = []
                location = []
                for val3 in range(0, 5):
                    values = [val1, val2, val3]
                    line.append(self.marks[values[ordering[0]]][values[ordering[1]]][values[ordering[2]]])
                    location += [values[ordering[0]], values[ordering[1]], values[ordering[2]]]
                if all(line):
                    lines.add(tuple(location))

            for val3 in range(0, 5):
                line = []
                location = []
                for val2 in range(0, 5):
                    values = [val1, val2, val3]
                    line.append(self.marks[values[ordering[0]]][values[ordering[1]]][values[ordering[2]]])
                    location += [values[ordering[0]], values[ordering[1]], values[ordering[2]]]
                if all(line):
                    lines.add(tuple(location))


            line = []
            location = []
            val3, val2, = 0, 0
            while val3 < 5 and val2 < 5:
                values = [val1, val2, val3]
                line.append(self.marks[values[ordering[0]]][values[ordering[1]]][values[ordering[2]]])
                location += [values[ordering[0]], values[ordering[1]], values[ordering[2]]]
                val3 += 1
                val2 += 1
            if all(line):
                lines.add(tuple(location))

            line = []
            location = []
            val3, val2 = 0, 4
            while val3 < 5 and val2 >= 0:
                values = [val1, val2, val3]
                line.append(self.marks[values[ordering[0]]][values[ordering[1]]][values[ordering[2]]])
                location += [values[ordering[0]], values[ordering[1]], values[ordering[2]]]
                val3 += 1
                val2 -= 1
            if all(line):
                lines.add(tuple(location))

        return lines


data = open('input.txt').read().splitlines()

numbers = []
cards = []

card_start = 0
for i in range(0, len(data)):
    if len(data[i]) == 0:
        card_start = i + 1
        break
    numbers += [int(x) for x in data[i].split()]

for i in range(card_start, len(data)):
    nums = [int(x) for x in data[i].split()]
    cards.append(Card(nums))

for n in numbers:
    bingos = 0
    for card in cards:
        bingos += card.play_number(n)
    if bingos >= 5:
        print(n)
        break


cards3D = []
for i in range(card_start, len(data), 5):
    card_nums = []
    for j in range(i, i+5):
        nums = [int(x) for x in data[j].split()]
        card_nums += nums
    cards3D.append(Card3D(card_nums))

for n in numbers:
    for card in cards3D:
        card.play_number(n)
    bingos = 0
    for card in cards3D:
        bingos += card.bingos()
    if bingos >= 5:
        print(n)
        break
