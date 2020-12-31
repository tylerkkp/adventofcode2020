# Advent of Code 2020

# Day 13 Solution part 1

timestamp = 1000390
x = 'x' #need to make the x-es in the list into strings
buslist = [13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17
]

buses = []

for i in range(len(buslist)):
    if isinstance(buslist[i], int):
        buses.append(buslist[i])

busmod = []
busdiv = []
busnext = []
busnextmod = []
for j in range(len(buses)):
    busmod.append(timestamp % buses[j])
    busdiv.append(timestamp // buses[j]) #floor division
    busnext.append((timestamp // buses[j] * buses[j]) + buses[j])
    busnextmod.append((timestamp // buses[j] * buses[j]) + buses[j] - timestamp)

combined = zip(buses, busmod, busdiv, busnext, busnextmod)

result = list(combined)

for k in range(len(result)):
    print(result[k])

print(9 * 17)

####################################################
'''
def checkval(stamp, bus):
    if stamp % bus == 0:
        return True
'''
testlist = []
testpass = False

# buslist = [7,13,x,x,59,x,31,19] # 1068781
# buslist = [17,x,13,19] # 3417
# buslist = [67,x,7,59,61] # 779210
# buslist = [67,7,x,59,61] # 1261476
# buslist = [1789,37,47,1889] # 1202161486

testis = []
for n in range(len(buslist)):
    if isinstance(buslist[n], int):
        testis.append(n)
        testlist.append(buslist[n])
        # testdict[n] = buslist[n]
print(testis)
numstomatch = len(testis)
print('nums to match:', numstomatch)

testdict = dict(zip(testis, testlist))

def countest(testnum, stamp):
    global numstomatch
    global testpass
    if testnum == numstomatch: #len(buslist):
        print('matching timestamp:', stamp)
        testpass = True

'''
# LIST VERSION
def stamptest(stamp):
    global testpass
    counter = 0
    for i in testis:
        if (stamp + i) % buslist[i] != 0: # should this != i or zero???
            return
        else:
            counter += 1
            if counter > 5:
                print('counter:', counter)
                print('timestamp:', stamp)
            countest(counter, stamp)
            continue
'''
# DICT VERSION
def stamptest(stamp):
    global testpass
    counter = 0
    for k, v in testdict.items():
        if (stamp + k) % v != 0: # should this != i or zero???
            return
        else:
            counter += 1
            if counter > 5:
                print('counter:', counter)
                print('timestamp:', stamp)
            countest(counter, stamp)
            continue
'''
smallest = min(testlist)
print(smallest)
'''
# WOW THIS IS HACKY - NOTICED THAT THE MATCHING TIMESTAMPS WERE INCREMENTING
# BY 6734444873, STARTING AT 5206161506

stampval = 5206161506
while not testpass:
    stampval += 6734444873 # buslist[testis[0]]
    stamptest(stampval)
