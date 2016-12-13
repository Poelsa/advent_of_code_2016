from collections import Counter

with open("6_input.txt") as textFile:
    all = [list(line.split()[0]) for line in textFile]

transposed = list(zip(*all))
print(transposed)
word = ""
for parentheses in transposed:
    col = "".join(parentheses)
    word += str(Counter(col).most_common()[-1][0])

print(word)
