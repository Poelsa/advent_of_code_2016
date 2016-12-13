import math

#read input list
f = open("2_input.txt")

pad = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

class keyPad:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setPos(self, button, direction):
        button += direction
        if button > 1:
            button = 1
        if button < -1:
            button = -1
        return button

    def button(self, commandList):
        for com in commandList:
            if com is 'R':
                self.x = self.setPos(self.x, 1)
            elif com is 'L':
                self.x = self.setPos(self.x, -1)
            elif com is 'U':
                self.y = self.setPos(self.y, 1)
            elif com is 'D':
                self.y = self.setPos(self.y, -1)

            #print(com + ": " + str(self.x) + " " + str(self.y))
        print(commandList + ": " + str(self.x) + " " + str(self.y))
        return pad[self.y+1][self.x+1]

current = keyPad()
num = ""
#print(commands)
for line in f:
    num += str(current.button(line))
print(num)

f.close()