# Advent of Code

# Day Five Solution

import pandas as pd

seatcodes = pd.read_csv('adventofcode2020_day5.csv', sep = '\n', names = ['seatcode'])

seatcodes['rowcodes'] = seatcodes['seatcode'].str[0:7]

seatcodes['colcodes'] = seatcodes['seatcode'].str[7:10]

'''
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

A = [1,2,3,4,5,6]
B, C = split_list(A)
'''

def firsthalf(rc_list):
    half = len(rc_list)//2
    return rc_list[:half]

def secondhalf(rc_list):
    half = len(rc_list)//2
    return rc_list[half:]

def indexfinder(code): #can input rowcode or colcode
    startint = 2 ** (len(code))
    seatrange = list(range(0, startint))

    for char in range(len(code)):
        if code[char] == 'F':
            seatrange = firsthalf(seatrange)
        if code[char] == 'L':
            seatrange = firsthalf(seatrange)
        if code[char] == 'B':
            seatrange = secondhalf(seatrange)
        if code[char] == 'R':
            seatrange = secondhalf(seatrange)
    print('code is:', seatrange[0])
    return seatrange[0]

# create new columns to contain the actual row or column id number
seatcodes['row_id'] = seatcodes['rowcodes']
seatcodes['col_id'] = seatcodes['colcodes']

# now apply the indexfinder function to the row/column code to find the id
seatcodes['row_id'] = seatcodes['row_id'].apply(indexfinder)
seatcodes['col_id'] = seatcodes['col_id'].apply(indexfinder)

# now multiply the row_id by the column_id to get the seat_id
seatcodes['seat_id'] = seatcodes['row_id'] * 8 + seatcodes['col_id']

print('biggest seat_id is:', seatcodes['seat_id'].max())

# Part 2
seatlist = (seatcodes['seat_id'].sort_values()).to_list()

for item in range(len(seatlist)-1):
    if seatlist[item] != seatlist[item + 1] - 1:
        print('Your seat is:', seatlist[item] + 1)
