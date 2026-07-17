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
     

data = open('input.txt').read().splitlines()

numbers = []
cards = []

i = 0
for i in range(0, len(data)):
    if len(data[i]) == 0:
        i += 1
        break
    numbers += [int(x) for x in data[i].split()]

for i in range(i, len(data)):
    nums = [int(x) for x in data[i].split()]
    cards.append(Card(nums))

for n in numbers:
    bingos = 0
    for card in cards:
        bingos += card.play_number(n)
    if bingos >= 5:
        print(n)
        break
