#!/usr/bin/python3
from collections import defaultdict

sum = 0
count = 0
nums = defaultdict(int)
digits = defaultdict(int)

with open('input.txt') as f:
    for line in f.read().splitlines():
        n = int(line)
        sum += n
        count += 1
        nums[n] += 1
        while n > 0:
            digits[n%10] += 1
            n //= 10

nums_s = sorted(nums.keys(), key=lambda x : nums[x], reverse=True)
digits_s = sorted(digits.keys(), key=lambda x : digits[x])

print(sum)
print(round(sum / count))
print(f"{nums_s[0]}{digits_s[0]}")
