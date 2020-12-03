# Advent of Code

# Day 1 Problem 1

import pandas as pd

nums = pd.read_csv('adventofcode2020_day1.csv')

numlist = nums.values.tolist()

flatList = [item for elem in numlist for item in elem]

for i in range(len(flatList)):
    testnum = int(flatList[i])
    neednum = 2020 - testnum
    if neednum in flatList:
        print(testnum * neednum)
        break
    else:
        continue

sortednums = sorted(flatList)

print(sortednums[::-1])

for x in range(len(sortednums)):
    num1 = sortednums[x]
    for y in range(x, len(sortednums)):
        num2 = sortednums[y]
        testnum = 2020 - num1 - num2
        if testnum in sortednums:
            print(testnum * num1 * num2)
            break
        else:
            continue
