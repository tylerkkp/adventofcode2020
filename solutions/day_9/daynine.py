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

res_len = len(results)

for i in range(25, res_len):
    testlist = results[i - 25: i]
    passtest = 0
    for j in range(len(testlist)):
        if results[i] - testlist[j] in testlist:
            passtest += 1
    if passtest == 0:
        print('part 1 solution:', results[i])
        break

revres = results[::-1]
breakloc = revres.index(2089807806)
revres = revres[breakloc:]
revres = revres[1:]

global testsize
testsize = 2
tlist = []


for i in range(len(revres)):
    tlist = []
    if revres[i] > 2089807806:
        continue
    for j in range(testsize):
        tlist.append(revres[i+j])
    listsum = sum(map(int, tlist))
    if listsum == 2089807806:
        finallist = tlist
        break
    elif listsum < 2089807806:
        testsize += 1
    else:
        continue

finallist = sorted(finallist)
print('part 2 solution:', finallist[0] + finallist[-1])
