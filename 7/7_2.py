import re


def isThing(t):
    if len(t) < 3:
        return []
    retArr = []
    for i in range(0, len(t)-2):
        if t[i] != t[i+1]:
            a = t[i:i+2]
            b = t[i+1:i+3][::-1]
            #print(a + " " + b)
            if t[i:i+2] == t[i+1:i+3][::-1]:
                retArr.append(t[i:i+3])
    return retArr

def isOtherThing(t, seq):
    if len(t) < 3:
        return False
    qes = seq[0:2][::-1] + seq[1]
    #print(seq + qes)
    for i in range(0, len(t)-1):
        if t[i:i+3] == qes:
            return True
    return False

def mainThing(line):
    line = line.strip()
    inBrackets = compReg.findall(line)
    for t in inBrackets:
        line = line.replace(t, '')
    outBrackets = line.split('[]')
    # print(inBrackets)
    # print(outBrackets)
    for text in outBrackets:
        thingies = isThing(text)
        if thingies:
            for brack in inBrackets:
                for seq in thingies:
                    if isOtherThing(brack, seq): return True
    return False

counter = 0
compReg = re.compile("\[([^]]*)\]")
with open("7_input.txt") as file:
    for line in file:
        if mainThing(line) == True:
            counter += 1

print(counter)