import hashlib

input = "cxdnnyjw"

out = ""
j = 0

for i in range(0,8):
    while True:
        curStr = input + str(j)
        hash = hashlib.md5(bytes(curStr.encode())).hexdigest()
        #print(hash)
        hashStr = str(hash)
        j += 1
        if hashStr.startswith('00000'):
            out += hashStr[5]
            print(hashStr)
            break

print(out)