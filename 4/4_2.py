from collections import Counter
from operator import itemgetter
import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shift %= 26
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

#read input list
f = open("4_input.txt")

allCorrectRooms = {}

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
        #print(letters)
        text = caesar(letters.lower(),int(code))
        #print(text)
        allCorrectRooms[text] = code

    #print('----------------')
for key, val in allCorrectRooms.items():
    if "north" in key.lower():
        print(key + ": " + val)

f.close()