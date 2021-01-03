# Advent of Code 2020

# Day 15 Solution part one

'''
In this game, the players take turns saying numbers. They begin by taking turns
reading from a list of starting numbers (your puzzle input). Then, each turn
consists of considering the most recently spoken number:

If that was the first time the number has been spoken, the current player says
0. Otherwise, the number had been spoken before; the current player announces
how many turns apart the number is from when it was previously spoken.
So, after the starting numbers, each turn results in that player speaking aloud
either 0 (if the last number is new) or an age (if the last number is a repeat).

Problem statement: What is the 2020th number spoken?
'''

input = [20,0,1,11,6,3]
# input = [1, 3, 2] # should return 1

turn = len(input)

def finddiff(lastnum, input):
    indexes = []
    for i in range(len(input)):
        if lastnum == input[i]:
            indexes.append(i)
    return indexes[-1] - indexes[-2]

def speak(turnnum, input):
    global turn
    lastnum = input[-1]
    turn += 1
    if lastnum in input[:-1]:
        diff = finddiff(lastnum, input)
        input.append(diff)
    else:
        input.append(0)


while turn < 2020:
    print(turn)
    speak(turn, input)

print(input[-1])
