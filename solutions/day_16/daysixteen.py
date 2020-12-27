# Advent of Code day 16

# Solution Part 1

import csv
from csv import reader
import pandas as pd

myticket = [127,83,79,197,157,67,71,131,97,193,181,191,163,61,53,89,59,137,73,167]

with open('adventofcode2020_day16_rules.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)

with open('adventofcode2020_day16_nearby.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    nearbylist = list(csv_reader)

validvalues = []

newlist = []
for i in range(len(list_of_rows)):
    newlist.append(list_of_rows[i][0].split(': ')[1])

splitlist = []
for j in range(len(newlist)):
    part1 = newlist[j].split(' or ')[0]
    part2 = newlist[j].split(' or ')[1]
    splitlist.append(part1)
    splitlist.append(part2)

for k in range(len(splitlist)):
    minnum = int(splitlist[k].split('-')[0])
    maxnum = int(splitlist[k].split('-')[1]) + 1
    numrange = range(minnum, maxnum)
    validvalues += numrange

validvalues = list(set(validvalues))

errorlist = []
for m in range(len(nearbylist)):
    for n in range(len(nearbylist[m])):
        if int(nearbylist[m][n]) not in validvalues:
            errorlist.append(nearbylist[m][n])

errorsum = 0
for o in range(len(errorlist)):
    errorsum += int(errorlist[o])
print(errorsum)
