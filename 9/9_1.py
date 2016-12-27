import re

def day9a(d):
    bracket = re.search(r'\((\d+)x(\d+)\)', d)
    if not bracket:
        return len(d)
    pos = bracket.start(0)
    sz = int(bracket.group(1))
    rpt = int(bracket.group(2))
    i = pos + len(bracket.group())
    return len(d[:pos]) + len(d[i:i+sz]) * rpt + day9a(d[i+sz:])

with open("9_input.txt") as file:
    marker = 0
    output = ""
    text = file.read().replace(' ', '')
    print(day9a(text))
    compReg = re.compile("\((\d+)x(\d+)\)")
    while True:
    #for i in range(3):
        match = compReg.search(text[marker:])
        #print("1: " + text[marker:])
        if match == None:# or marker > len(text):
            break
        #print("2: Marker: " + str(marker) + " matchstart: " + str(match.start()))
        output += text[marker:marker + match.start()]
        #print("3: " + match.group())
        numChars = int(match.group(1))
        multi = int(match.group(2))
        #print("4: " + str(numChars) + "x" + str(multi))
        marker += match.end()
        #print("5: " + text[marker:marker+numChars] * multi)
        output += text[marker:marker+numChars] * multi
        marker += numChars
        #print("----------")

    if marker != len(text):
        output += text[marker:]

print(len(output))
#print(output)


