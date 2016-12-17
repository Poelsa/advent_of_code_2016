width = 50
height = 6
grid = [x[:] for x in [[0] * height] * width]

def lightRect(x, y):
    for i in range(0,x):
        for j in range(0,y):
            grid[i][j] = 1

def rotRow(row, n):
    for i in range(0, n):
        lastPixel = grid[-1][row]
        for x in range(0, width):
            currentPixel = grid[x][row]
            grid[x][row] = lastPixel
            lastPixel = currentPixel


def rotCol(col, n):
    for i in range(0, n):
        lastPixel = grid[col][-1]
        for y in range(0, height):
            currentPixel = grid[col][y]
            grid[col][y] = lastPixel
            lastPixel = currentPixel

with open("8_input.txt") as file:
    for line in file:
        if "rect" in line:
            arr = line.split()
            coord = arr[1].split('x')
            lightRect(int(coord[0]), int(coord[1]))
        elif "row" in line:
            arr = line.split()
            row = arr[2].split('=')
            rotRow(int(row[1]), int(arr[4]))
        elif "col" in line:
            arr = line.split()
            col = arr[2].split('=')
            rotCol(int(col[1]), int(arr[4]))

bap = list(zip(*grid))
print(bap)
