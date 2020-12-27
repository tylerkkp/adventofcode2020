# Advent of Code day 22

# Solution part 1

p1 = [6, 25, 8, 24, 30, 46, 42, 32, 27, 48, 5, 2, 14, 28, 37, 17, 9, 22, 40, 33, 3, 50, 47, 19, 41]
p2 = [1, 18, 31, 39, 16, 10, 35, 29, 26, 44, 21, 7, 45, 4, 20, 38, 15, 11, 34, 36, 49, 13, 23, 43, 12]

emptytest = False
finaldeck = []

def round(p1, p2):
    global emptytest
    if len(p1) == 0:
        emptytest = True
        return
    if len(p2) == 0:
        emptytest = True
        return
    var1 = p1.pop(0)
    var2 = p2.pop(0)
    if var1 > var2:
        result = [var1, var2]
        p1 += result
        print('p1 =', p1)
    else:
        result = [var2, var1]
        p2 += result
        print('p2 =', p2)

while not emptytest:
    round(p1, p2)

if len(p1) == 0:
    winner = 'p2'
    finaldeck = p2
else:
    winner = 'p1'
    finaldeck = p1

print(winner + '=', finaldeck)
print(len(finaldeck))

multlist = []
for i in range(len(finaldeck)):
    multlist.append(i + 1)

multlist.sort(reverse = True)

totalscore = 0
for i in range(len(finaldeck)):
    totalscore += finaldeck[i] * multlist[i]

print(totalscore)
