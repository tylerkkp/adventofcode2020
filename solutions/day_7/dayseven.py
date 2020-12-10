# Advent of Code Day 7

# Solution part 1

import pandas as pd
import csv
from string import digits
import re

results = []
with open('adventofcode2020_day7.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split('.'))

ruleslist = []
for i in range (len(results)):
    rem_digits = str.maketrans('', '', digits)
    r_nodigs = results[i][0].translate(rem_digits)
    r_nobags = re.sub(r'(bags|bag)', ',', r_nodigs) #replace 'bag(s)' with ','
    r_nodots = re.sub(r'(\.)', '', r_nobags) #remove periods
    r_notrail = re.sub(r'(\s\,)', ',', r_nodots) #remove extra spaces
    r_noxtra_ = re.sub(r'(\s\s)', ' ', r_notrail) #remove extra spaces
    r_final = re.sub(r'(\,\,)', ',', r_noxtra_) #remove extra commas
    r_final = r_final[:-1] #remove trailing commas
    ruleslist.append(r_final)

bag_of_dicts = {}
colorset = set()

for j in range(len(ruleslist)):
    entry = ruleslist[j].partition(', contain')[0]
    templist = ruleslist[j].partition('contain ')[2].split(', ')
    bag_of_dicts[entry] = templist

print(bag_of_dicts)

gold = 'shiny gold'
colorlist = ['shiny gold']
colors = []

def colortest(str, list):
    if str in list:
        return True

for m in bag_of_dicts.keys():
    for i in range(len(colorlist)):
        if colortest(colorlist[i], bag_of_dicts[m]):
            colors.append(m)
            print('m:', m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)
            print('m:', m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)
            print('m:', m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)
            print('m:', m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)
            print('m:', m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)
            print('m:', m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)
            print('m:', m)

colors = list(set(colors))
print('total:', len(colors))


#print(set(output))
#print(len(set(output)))
