import hashlib

input = "cxdnnyjw"
valid = ['0','1','2','3','4','5','6','7']

out = [None]*8
j = 0

for i in range(0,8):
    while True:
        curStr = input + str(j)
        hash = hashlib.md5(bytes(curStr.encode())).hexdigest()
        #print(hash)
        hashStr = str(hash)
        j += 1
        if hashStr.startswith('00000') and hashStr[5] in valid:
            out[int(hashStr[5])] = hashStr[6]
            valid.remove(hashStr[5])
            print("".join(hashStr))
            break

print(out)