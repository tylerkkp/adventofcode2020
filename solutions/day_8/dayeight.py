# Advent of Code Day 8

# Solution Part 1

import pandas as pd
import time

input = pd.read_csv('adventofcode2020_day8.csv', names = ['command'])
input['action_num'] = input.index
input = input[['action_num', 'command']]
input = input.astype(str)
print(input['command'][5])
#split on the whitespace
input['cmd'] = input['command'].str.split(' ')
#extract the + or - sign from the numeric value
input['sign'] = input['cmd'].str[1].str[0]
#extract the number
input['amt'] = input['cmd'].str[1].str[1:]
#pare down the 'cmd' column to be just the 3 letter command acc/jmp/nop
input['cmd'] = input['cmd'].str[0]

print(input.head(20))

#append action numbers to runlist to make sure they are only run once
runlist = []

norepeats = True

acc = 0
opnum = 0

def runtest(action):
    if action in runlist:
        return True

def run_act(operation):
    global acc
    global opnum
    print(runlist)
    print('acc:', acc)
    if runtest(int(operation)):
        norepeats = False
        #return acc
    #runlist.append(opnum)
    elif input['cmd'][operation] == 'acc':
        if input['sign'][operation] == '+':
            runlist.append(int(operation))
            acc += int(input['amt'][operation])
            opnum += 1
        else:
            runlist.append(int(operation))
            acc -= int(input['amt'][operation])
            opnum += 1
    elif input['cmd'][operation] == 'nop':
        runlist.append(operation)
        opnum += 1
    else:
        if input['sign'][operation] == '+':
            runlist.append(int(operation))
            opnum += int(input['amt'][operation])
        else:
            runlist.append(int(operation))
            opnum -= int(input['amt'][operation])

while norepeats:
    run_act(opnum)
    time.sleep(0.5)
