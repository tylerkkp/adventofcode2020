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
