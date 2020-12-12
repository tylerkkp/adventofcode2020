# Advent of Code Day 12

# Solution part 1

import csv
from string import digits
import re

inputlist = []
with open('adventofcode2020_day12.txt') as inputfile:
    for line in inputfile:
        inputlist.append(line.strip())

dir = []
for i in range(len(inputlist)):
    dir.append(inputlist[i][0])

dist = []
for j in range(len(inputlist)):
    dist.append(int(inputlist[j][1:]))

pos = [0, 0]
facing = 'E'

def move(direction, distance):
    if direction == 'F':
        direction = facing
    if direction == 'N':
        pos[1] += distance
    if direction == 'S':
        pos[1] -= distance
    if direction == 'E':
        pos[0] += distance
    if direction == 'W':
        pos[0] -= distance

def turn(direction, rotation):
    global facing
    dirlist = ['N', 'W', 'S', 'E']
    if direction == 'L':
        dir_then = dirlist.index(facing) #yields index of current direction
        if rotation == 90:
            facing = dirlist[dir_then - 3]
        if rotation == 180:
            facing = dirlist[dir_then - 2]
        if rotation == 270:
            facing = dirlist[dir_then - 1]
    if direction == 'R':
        dir_then = dirlist.index(facing) #yields index of current direction
        if rotation == 90:
            facing = dirlist[dir_then - 1]
        if rotation == 180:
            facing = dirlist[dir_then - 2]
        if rotation == 270:
            facing = dirlist[dir_then - 3]

for k in range(len(inputlist)):
    if (dir[k] == 'L') or (dir[k] == 'R'):
        turn(dir[k], dist[k])
    else:
        move(dir[k], dist[k])
    # print('position:', pos, '- now facing:', facing)

print('final position:', pos)
print(abs(pos[0]) + abs(pos[1]))
