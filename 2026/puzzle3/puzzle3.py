#!/usr/bin/python3

def password_score(password):
    upper, lower, digit = False, False, False
    score = 0

    for ch in password:
        if not upper and ch.isupper():
            upper = True
            score += 1
        elif not lower and ch.islower():
            lower = True
            score += 1
        elif not digit and ch.isdigit():
            digit = True
            score += 1

        if score == 3:
            break

    return score * len(password)


max_score = 0
max_password = ""

f = open('input.txt')
for line in f.read().splitlines():
    score = password_score(line)
    if score > max_score:
        max_score = score
        max_password = line

print(max_password)
