# Advent of Code Day 10

# Solution Part 1

import pandas as pd

adaptor_df = pd.read_csv('adventofcode2020_day10.csv', names = ['adaptor'])

adaptor_df = adaptor_df.sort_values(by = 'adaptor', ascending = True)

adaptorlist = adaptor_df.values.tolist()

a_int_list = [0]
for i in range(len(adaptorlist)):
    a_int_list.append(adaptorlist[i][0])

a_int_list.append(a_int_list[-1] + 3) #adding the max joltage

print(a_int_list[0])

count1 = 0
count3 = 0

for j in range(len(a_int_list) - 1):
    bigger = a_int_list[j+1]
    smaller = a_int_list[j]
    if bigger - smaller == 1:
        count1 += 1
    if bigger - smaller == 3:
        count3 += 1

print('1 jolt gaps:', count1)
print('3 jolt gaps:', count3)
print(len(a_int_list))

print(count1 * count3)
