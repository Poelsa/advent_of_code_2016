
def isValidTriangle(nums):
    maxS = max(nums[0], max(nums[1], nums[2]))
    nums.remove(maxS)
    if maxS < nums[0] + nums[1]:
        return 1
    else:
        return 0

#read input list
f = open("3_input.txt")

nrOfCorrectTriangles = 0

all = f.read()
all = all.splitlines()
for i in range(0, len(all), 3):
    row1 = [int(j) for j in all[i].split()]
    row2 = [int(j) for j in all[i+1].split()]
    row3 = [int(j) for j in all[i+2].split()]

    nrOfCorrectTriangles += isValidTriangle([row1[0], row2[0], row3[0]])
    nrOfCorrectTriangles += isValidTriangle([row1[1], row2[1], row3[1]])
    nrOfCorrectTriangles += isValidTriangle([row1[2], row2[2], row3[2]])

print(nrOfCorrectTriangles)

f.close()