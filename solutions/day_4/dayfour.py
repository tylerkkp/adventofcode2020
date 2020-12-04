# Advent of Code

# Day Four Solutions

import pandas as pd
import csv
from re import search

inputdf = pd.read_csv('adventofcode2020_day4.csv', skip_blank_lines = False, names = ['vals'])
inputlist = inputdf.values.tolist()

nancount = 0

inputstr = ''
for item in range(len(inputlist)):
    teststr = str(inputlist[item][0])
    if teststr != 'nan':
        inputstr = inputstr + teststr
    else:
        inputstr = inputstr + ','


''' List of required fields
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

testfields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
passcount = 0

''' List of required tests
byr (Birth Year) - four digits; at least 1920 and at most 2002.      ### (byr:)(19[2-8][0-9]|199[0-9]|200[0-2])
iyr (Issue Year) - four digits; at least 2010 and at most 2020.      ### (iyr:)(201[0-9]|2020)
eyr (Expiration Year) - four digits; at least 2020 and at most 2030. ### (eyr:)(202[0-9]|2030)
hgt (Height) - a number followed by either cm or in:                 ### (hgt:)
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.### (#([0-9|[a-f][0-9|[a-f][0-9|[a-f][0-9|[a-f][0-9|[a-f][0-9|[a-f]]))
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.       ### (ecl:)(amb|blu|brn|gry|grn|hzl|oth)
pid (Passport ID) - a nine-digit number, including leading zeroes.   ### (pid:)[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
cid (Country ID) - ignored, missing or not.
'''

''' REGEX SEARCH
newlist = inputstr.split(',')
print(len(newlist))

from re import search
fullstring = "StackAbuse"
substring = "tack"
if search(substring, fullstring):
    print "Found!"
else:
    print "Not found!"
'''

def teststr(str1, testlist):
    testcount = 0
    testlen = len(testlist)
    for x in range(testlen):
        if testlist[x] in str1:
            testcount += 1
            if testcount == testlen:
                return True


for i in range(len(newlist)):
    if teststr(newlist[i], testfields) == True:
        passcount += 1


print(newlist[0:10])
print('nancount =', nancount)
print('newlist length: ', len(newlist))
print(passcount)
