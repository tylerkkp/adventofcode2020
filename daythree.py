# Advent of Code 2020

# Day 3 Problem 1

import pandas as pd

skiinput = pd.read_csv('adventofcode2020_day3.csv', names = ['rows'])

skilist = skiinput['rows'].tolist()

treecounter = 0

wraplen = len(skilist[0]) - 1 # yields max index - 30 in this case

skipos = 0
''' Solution for part 1
for row in range(len(skilist)):
    if skilist[row][skipos] == '#':
        treecounter += 1
        print(row, skipos, ' tree!')
    skipos += 3
    if skipos > wraplen:
        skipos = skipos - wraplen - 1

print(treecounter)
'''
### PART TWO
'''
# Solution for part 2 - right1, down 1
for row in range(len(skilist)):
    if skilist[row][skipos] == '#':
        treecounter += 1
        print(row, skipos, ' tree!')
    skipos += 1
    if skipos > wraplen:
        skipos = skipos - wraplen - 1

print(treecounter)
# 86

# Result for the second part from above: 159

# Solution for part 2 - right 5, down 1
for row in range(len(skilist)):
    if skilist[row][skipos] == '#':
        treecounter += 1
        print(row, skipos, ' tree!')
    skipos += 5
    if skipos > wraplen:
        skipos = skipos - wraplen - 1

print(treecounter)
# 97


# Solution for part 2 - right 7, down 1
for row in range(len(skilist)):
    if skilist[row][skipos] == '#':
        treecounter += 1
        print(row, skipos, ' tree!')
    skipos += 7
    if skipos > wraplen:
        skipos = skipos - wraplen - 1

print(treecounter)
# 88
'''

# Solution for part 2 - right 1, down 2
for row in range(len(skilist)):
    if (row + 1) % 2 == 0:
        continue
    if skilist[row][skipos] == '#':
        treecounter += 1
        print(row, skipos, ' tree!')
    skipos += 1
    if skipos > wraplen:
        skipos = skipos - wraplen - 1

print(treecounter)
# 55
