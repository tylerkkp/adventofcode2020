# Advent of Code day 9

# Solution part 1

import pandas as pd
import csv
from string import digits
import re

results = []
with open('adventofcode2020_day9.txt') as inputfile:
    for line in inputfile:
        results.append(int(line.strip()))

print(results[0:25])

res_len = len(results)

for i in range(25, res_len):
    testlist = results[i - 25: i]
    passtest = 0
    for j in range(len(testlist)):
        if results[i] - testlist[j] in testlist:
            passtest += 1
    if passtest == 0:
        print(results[i])
        break
