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

# print(bag_of_dicts)

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

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)

for m in bag_of_dicts.keys():
    colors = list(set(colors))
    for i in range(len(colors)):
        if colortest(colors[i], bag_of_dicts[m]):
            colors.append(m)

colors = list(set(colors))
print('total:', len(colors))


#print(set(output))
#print(len(set(output)))


colortree = ['shiny gold']

for m in bag_of_dicts.keys():
    if m == colortree[0]:
        for i in range(len(bag_of_dicts[m])):
            colortree.append(bag_of_dicts[m][i])
    colortree = list(set(colortree))
print('colortree =', colortree)


for m in bag_of_dicts.keys():
    for n in range(len(colortree)):
        if m == colortree[n]:
            for i in range(len(bag_of_dicts[m])):
                colortree.append(bag_of_dicts[m][i])
    colortree = list(set(colortree))
print('colortree =', colortree)

for m in bag_of_dicts.keys():
    for n in range(len(colortree)):
        if m == colortree[n]:
            for i in range(len(bag_of_dicts[m])):
                colortree.append(bag_of_dicts[m][i])
    colortree = list(set(colortree))
print('colortree =', colortree)
print('colortree len:', len(colortree))


for m in bag_of_dicts.keys():
    for n in range(len(colortree)):
        if m == colortree[n]:
            for i in range(len(bag_of_dicts[m])):
                colortree.append(bag_of_dicts[m][i])
    colortree = list(set(colortree))
print('colortree =', colortree)
print('colortree len:', len(colortree))
colortree.remove('no other')
print('colortree =', colortree)
print('colortree len:', len(colortree))

### end of part 1 ###################################################

print('\n')
print('#' * 100)
print('\n')
testlist = [['']]

for x in range(len(results)):
    nobags = re.sub(r'(bags|bag)', ',', results[x][0]) #replace 'bag(s)' with ','
    testlist.append(nobags)
    #print('"'+nobags+'"')

def find(string, sample) :
    if (sample in string):
        y = "^" + sample
        x = re.search(y, string)
        if x :
            return True
        else :
            return False

finallist = []
for y in range(len(testlist)):
    for z in range(len(colortree)):
        if find(colortree[z][0], testlist[y][0]):
            if testlist[y] in finallist:
                continue
            else:
                finallist.append(testlist[y])

############### NEED TO EDIT BELOW ############################

strlist = []
for i in range (len(finallist)):
    if i == 0:
        continue
    else:
        r_nodots = re.sub(r'(\.)', '', finallist[i]) #remove periods
        r_notrail = re.sub(r'(\s\,)', ',', r_nodots) #remove extra spaces
        r_noxtra_ = re.sub(r'(\s\s)', ' ', r_notrail) #remove extra spaces
        r_final = re.sub(r'(\,\,)', ',', r_noxtra_) #remove extra commas
        r_final = r_final[:-1] #remove trailing commas
        strlist.append(r_final)

print(strlist)

###############################################################

for line in range(len(strlist)):
    print(strlist[line])
print(len(strlist))

for line in range(len(strlist)):
    firsthalf = strlist[line].split(', contain')[0]
    sechalf = strlist[line].split(', contain')[1:]
    if 'shiny gold' in firsthalf:
        print('shiny gold contains:', sechalf)
        print(strlist[line])

for line in range(len(strlist)):
    firsthalf = strlist[line].split(', contain')[0]
    sechalf = strlist[line].split(', contain')[1:]
    if 'vibrant blue' in firsthalf:
        print('vibrant blue contains:', sechalf)
        print(strlist[line])

def searchbags(bagcolor):
    for line in range(len(strlist)):
        firsthalf = strlist[line].split(', contain')[0]
        sechalf = strlist[line].split(', contain')[1:]
        if bagcolor in firsthalf:
            print(bagcolor,' contains:', sechalf)
            print(strlist[line])


'''
if (contents) == 'no other':
'''
