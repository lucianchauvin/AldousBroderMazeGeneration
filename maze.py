import random
import keyboard
from PIL import Image
from scipy.interpolate import interp1d

w, h = 1920, 1080


def p(m):
    print("-" * w)
    for r in m:
        x = ""
        for c in r:
            x += str(c)
        print(x)
    print("-" * w)


def checkvalid(m, x, y):
    try:
        h = m[x][y]
        return True
    except:
        return False


# Aldous-Broder algorithm

grid = [[1 for x in range(w)] for y in range(h)]

totalc = w*h/4

x, y = 0, 0
grid[x][y] = 0
totalc -= 1

while totalc > 0:
    print(totalc)
    dir = random.randint(0, 3)
    if(dir == 0):
        if checkvalid(grid, x, y - 2):
            y -= 2
            if grid[x][y] != 0:
                totalc -= 1
                grid[x][y] = 0
                grid[x][y+1] = 0
    elif(dir == 1):
        if checkvalid(grid, x, y + 2):
            y += 2
            if grid[x][y] != 0:
                totalc -= 1
                grid[x][y] = 0
                grid[x][y-1] = 0
    elif(dir == 2):
        if checkvalid(grid, x+2, y):
            x += 2
            if grid[x][y] != 0:
                totalc -= 1
                grid[x][y] = 0
                grid[x-1][y] = 0
    elif(dir == 3):
        if checkvalid(grid, x-2, y):
            x -= 2
            if grid[x][y] != 0:
                totalc -= 1
                grid[x][y] = 0
                grid[x+1][y] = 0


# Image

img = Image.new('RGB', (w, h), "black")
pixels = img.load()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if grid[y][x] == 0:
            pixels[x, y] = (255, 255, 255)

img.save("maze.png")
