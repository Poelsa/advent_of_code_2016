import math

#read input list
f = open("2_input.txt")

pad = [[' ',' ','D',' ',' '],
       [' ','A','B','C',' '],
       ['5','6','7','8','9'],
       [' ','2','3','4',' '],
       [' ',' ','1',' ',' ']]

class keyPad:
    def __init__(self):
        self.x = -2
        self.y = 0

    def setPos(self, x, y, dx, dy):
        x += dx
        y += dy

        ax = abs(x)
        ay = abs(y)

        if (ax == 1 and ay == 2) or \
            (ax == 2 and ay == 2) or \
            (ax == 2 and ay == 1) or \
            (ax > 2) or (ay > 2):
            x -= dx
            y -= dy

        if dx != 0:
            return x
        else:
            return y

    def button(self, commandList):
        for com in commandList:
            if com is 'R':
                self.x = self.setPos(self.x, self.y, 1, 0)
            elif com is 'L':
                self.x = self.setPos(self.x, self.y, -1, 0)
            elif com is 'U':
                self.y = self.setPos(self.x, self.y, 0, 1)
            elif com is 'D':
                self.y = self.setPos(self.x, self.y, 0, -1)

            #print(com + ": " + str(self.x) + " " + str(self.y))
        print(commandList + ": " + str(self.x) + " " + str(self.y))
        return pad[self.y+2][self.x+2]

current = keyPad()
num = ""
#print(commands)
for line in f:
    num += str(current.button(line))
print(num)

f.close()