#read input list
f = open("3_input.txt")

nrOfCorrectTriangles = 0

for l in f:
    nums = [int(i) for i in l.split()]
    maxS = max(nums[0], max(nums[1], nums[2]))
    nums.remove(maxS)
    if maxS < nums[0] + nums[1]:
        nrOfCorrectTriangles += 1

print(nrOfCorrectTriangles)

f.close()