# Advent of Code day 6

# Solution to part 1

import pandas as pd
import csv
import re

groupsdf = pd.read_csv('adventofcode2020_day6.csv', skip_blank_lines = False, names = ['vals'], engine = 'python')
grouplist = groupsdf.values.tolist()

inputstr = ''
for i in range(len(grouplist)):
    inputstr += str(grouplist[i][0])

inputlist = inputstr.split('None')

groupcounts = 0

for j in range(len(inputlist)):
    splitchars = list(inputlist[j])
    uniquechars = list(set(splitchars))
    groupcounts += (len(uniquechars))

print('sum =', groupcounts)

# Part 2
newlist = groupsdf.values.tolist()


def in_str(str, char):
    if char in list(str):
        return True

def group_count(list):
    count = len(list)
    return count

def test_set(lista):
    tempstr = ''
    for b in range(len(lista)):
        tempstr += lista[b]
    tempstr = list(set(list(tempstr)))
    return tempstr

counter = 0

templist = []
for item in range(len(newlist)):
    if newlist[item][0] != None: #this is bad because it doesn't initiate count for the final group
        templist.append(newlist[item][0])
    else:
        groupcount = group_count(templist) # int of number of ppl in group
        testset = test_set(templist)
        for item in range(len(testset)):
            testcounter = 0
            for person in range(groupcount):
                if in_str(templist[person], testset[item]):
                    testcounter += 1
            if testcounter == groupcount:
                counter += 1
        templist = []

print('count is:', counter)


''' Used for testing final group only
triallist = ['dwqxfekvtn', 'wknsetqdfxv', 'dfqknxevtw', 'edtwfqxvnk', 'wtfkmrdhevqnx']
counter = 0
for item in range(len(triallist)):

        groupcount = group_count(triallist) # int of number of ppl in group
        testset = test_set(triallist)
        for item in range(len(testset)):
            testcounter = 0
            for person in range(groupcount):
                if in_str(triallist[person], testset[item]):
                    testcounter += 1
            if testcounter == groupcount:
                counter += 1
                print(triallist, counter)
        templist = []

print('count is:', counter)
'''
