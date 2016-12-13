import math

#read input list
f = open("1_input.txt")

class pointAndDir:
    def __init__(self):
        self.x = 0
        self.y = 0
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

        self.x += move * int(math.cos(math.radians(self.curDir)))
        self.y += move * int(math.sin(math.radians(self.curDir)))
        print("facing " + str(self.curDir) + " degrees, moving " + str(move) + " steps")
        print("currently at x: " + str(self.x) + " y: " + str(self.y))

current = pointAndDir()

line = f.read()
commands = line.split(', ')
#print(commands)
for command in commands:
    current.move(command)

print(abs(current.x))
print(abs(current.y))
print(abs(current.x) + abs(current.y))

f.close()