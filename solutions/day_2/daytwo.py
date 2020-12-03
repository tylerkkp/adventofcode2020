#day two test

# sample input:
# 7-13 j: tpscbbstbdjsjbtcpj
# sample output: 3 --> false

import pandas as pd

passdata = pd.read_csv('adventofcode2020_day2.csv', names = ['password'], engine = 'python')
passlist = passdata['password'].to_list()

validcount = 0

'''
def test_pwd(str1):
    strlist = str1.split(' ')
    minct, maxct = strlist[0].split('-')
    minct = int(minct)
    maxct = int(maxct)
    password = strlist[2]
    testltr = strlist[1].strip(':')
    ltrcount = password.count(testltr)
    if minct <= ltrcount <= maxct:
        validcount += 1;
'''

''' Part 1
for item in range(len(passlist)):
    str1 = passlist[item]
    strlist = str1.split(' ')
    minct, maxct = strlist[0].split('-')
    minct = int(minct)
    maxct = int(maxct)
    password = strlist[2]
    testltr = strlist[1].strip(':')
    ltrcount = password.count(testltr)
    if minct <= ltrcount <= maxct:
        validcount += 1;
'''

for item in range(len(passlist)):
    matchcount = 0
    str1 = passlist[item]
    strlist = str1.split(' ')
    opt1, opt2 = strlist[0].split('-')
    opt1 = int(opt1)
    opt2 = int(opt2)
    password = strlist[2]
    test1 = password[opt1 -1]
    test2 = password[opt2 - 1]
    testltr = strlist[1].strip(':')
    if test1 == testltr:
        matchcount += 1;
    if test2 == testltr:
        matchcount += 1;
    if matchcount == 1:
        validcount += 1


print('valid passwords: ', validcount)
