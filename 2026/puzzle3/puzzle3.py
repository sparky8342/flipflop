#!/usr/bin/python3
import re
import string

def password_score(password, additional_rules):
    score = 0

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if additional_rules:
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

def best_password(passwords, additional_rules):
    max_score = 0
    max_password = ""
    for password in passwords:
        score = password_score(password, additional_rules)
        if score > max_score:
            max_score = score
            max_password = password
    return max_password


passwords = open('input.txt').read().splitlines()

part1 = best_password(passwords, False)
part2 = best_password(passwords, True)

best_total = 0
for ch in string.ascii_lowercase + string.ascii_uppercase + string.digits:
    total = 0
    for password in passwords:
        password += ch
        total += password_score(password, True)

    if total > best_total:
        best_total = total

part3 = best_total

print(f"{part1}\n{part2}\n{part3}")
