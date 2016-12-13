import re


def isThing(t):
    if len(t) < 4:
        return False
    for i in range(0, len(t)-1):
        if t[i] != t[i+1]:
            if t[i:i+2] == t[i+2:i+4][::-1]:
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
        if isThing(text):
            for brack in inBrackets:
                if isThing(brack): return False
            return True

counter = 0
compReg = re.compile("\[([^]]*)\]")
with open("7_input.txt") as file:
    for line in file:
        if mainThing(line) == True:
            counter += 1

print(counter)