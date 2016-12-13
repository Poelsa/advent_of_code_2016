from collections import Counter
from operator import itemgetter

#read input list
f = open("4_input.txt")

sum = 0

for l in f:
    split = l.split('-')
    #print(split)
    code = split[-1].split('[')[0]
    #print(code)
    chksum = split[-1].split('[')[1].rstrip('\n')[:-1]
    #print(chksum)
    letters = "".join(split[:-1])
    #print(letters)
    c = Counter(letters)
    mc = c.most_common()
    #print('mc')
    #print(mc)

    sAlpha = sorted(mc, key=itemgetter(0))
    sCorr = sorted(sAlpha, key=itemgetter(1), reverse=True)
    #print(sCorr)
    arrayThingy = []
    [arrayThingy.append(elem[0]) for elem in sCorr]
    res = "".join(arrayThingy[:5])
    #print(res)

    if res == chksum:
        sum += int(code)

    #print('----------------')

print(sum)

f.close()