#!/usr/bin/python3
import re
import string

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


def password_score2(password):
    score = 0

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1
        if re.search("7", password) and not re.search("[0-68-9]", password):
            score += 7

    max_l = 0
    matches = re.findall("(.)(\\1+)", password)
    for match in matches:
        if len(match[1]) > max_l:
            max_l = len(match[1])

    max_l += 1
    if max_l >= 3:
        score += max_l * max_l

    if re.search("(red|green|blue)", password):
        score *= 3

    return score * len(password)

passwords = open('input.txt').read().splitlines()

max_score = 0
max_password = ""

for password in passwords:
    score = password_score(password)
    if score > max_score:
        max_score = score
        max_password = password

print(max_password)

max_score = 0
max_password = ""

for password in passwords:
    score = password_score2(password)
    if score > max_score:
        max_score = score
        max_password = password

print(max_password)

best_sum = 0
for ch in string.ascii_lowercase + string.ascii_uppercase + string.digits:
    sum = 0
    for password in passwords:
        password += ch
        sum += password_score2(password)

    if sum > best_sum:
        best_sum = sum

print(best_sum)
