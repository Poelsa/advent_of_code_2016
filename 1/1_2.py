import math

startX = 200
startY = 200

#read input list
f = open("1_input.txt")

class pointAndDir:
    def __init__(self):
        w, h = startX*2, startX*2
        #0=unvisited, 1=visited
        self.x = startX
        self.y = startY
        self.grid = [[0 for x in range(w)] for y in range(h)]
        self.grid[startX][startY] = 1
        self.curDir = 0

    def move(self, command):
        #get dir
        turn = command[0]
        if turn is 'R':
            self.curDir += 90
        elif turn is 'L':
            self.curDir -= 90
        self.curDir %= 360

        move = int(command[1:])
        for i in range(move):
            self.x += int(math.cos(math.radians(self.curDir)))
            self.y += int(math.sin(math.radians(self.curDir)))
            if self.grid[self.x][self.y] is 1:
                print("Been here before!")
                return 1
            self.grid[self.x][self.y] = 1
            print("facing " + str(self.curDir) + " degrees, moving one step")
            print("currently at x: " + str(self.x) + " y: " + str(self.y))
        return 0

current = pointAndDir()

line = f.read()
commands = line.split(', ')
#print(commands)
for command in commands:
    if current.move(command) is 1:
        break

print(abs(current.x-startX))
print(abs(current.y-startY))
print(abs(current.x-startX) + abs(current.y-startY))

f.close()