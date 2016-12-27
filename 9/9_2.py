import re

def day9b(d):
    bracket = re.search(r'\((\d+)x(\d+)\)', d)
    if not bracket:
        return len(d)
    pos = bracket.start(0)
    sz = int(bracket.group(1))
    rpt = int(bracket.group(2))
    i = pos + len(bracket.group())
    return len(d[:pos]) + day9b(d[i:i+sz]) * rpt + day9b(d[i+sz:])

with open("9_input.txt") as file:
    marker = 0
    output = ""
    text = file.read().replace(' ', '')
    print(day9b(text))
    compReg = re.compile("\((\d+)x(\d+)\)")
    newString = text
    while True:
    #for i in range(3):
        match = compReg.search(newString)
        #print("1: " + text[marker:])
        if match == None:# or marker > len(text):
            break
        #print("2: Marker: " + str(marker) + " matchstart: " + str(match.start()))
        #output += text[marker:marker + match.start()]
        #print("3: " + match.group(1))
        numChars = int(match.group(1))
        multi = int(match.group(2)) - 1
        #print("4: " + str(numChars) + "x" + str(multi))
        marker = match.end()
        #print("5: " + text[marker:marker+numChars] * multi)
        #output += text[marker:marker+numChars] * multi
        #print(match.group())
        newString = newString.replace(match.group(), newString[marker:marker+numChars]*multi)
        #print(newString[marker:marker+numChars]*multi)
        #marker += len(match.group())
        #print("----------")
    output += newString


print(len(output))
#print(output)


