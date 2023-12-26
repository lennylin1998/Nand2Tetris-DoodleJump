from tkinter import W
from PIL import Image
from bitstring import Bits
import os
os.chdir("/Users/powen/Desktop/nand2tetris/projects/PacMan-nand2tetris-main")
print("Current Working Directory:", os.getcwd())

w = 2
h = 2

nW = w * 16
nH = h * 16



# im = Image.open(r"./images/gameover.png")
im = Image.open("./images/gray.jpg")
im = im.resize((nW, nH))
pix = im.load()

grid = [[0 for x in range(nW)] for y in range(nH)]

print(im.mode)

def writeToFile(grid):
    i = 0
    with open('./images/converted.txt', 'w') as f:
        for g in grid:
            converted = lambda g, x: [g[i:i+x] for i in range(0, len(g), x)]

            for j in range(w):
                bina = "".join([str(x) for x in converted(g, 16)[j]])[::-1]
                a = Bits(bin=bina)
                #to_write = f" let sprite[{i}] = {a.int};\n"
                num = a.int
                if (num != 0 and num > -32000 and num < 32000):
                    to_write = f"do Memory.poke(memAddress + {i * 32 + j}, {a.int});\n"
                    f.write(to_write)
            i += 1

factor = 100

for i in range(nH):
    for j in range(nW):
        p = pix[j, i]
        if (p[0] > 0 and p[0] < factor or p[1] > 0 and p[1] < factor or p[2] > 0 and p[2] < factor):
            pix[j, i] = (0, 0, 0, 255)
            grid[i][j] = 1
        else:
            pix[j, i] = (255, 255, 255, 255)



print("black")
for j in range(nW):
    print(" ")
    for i in range(nH):
        if (grid[i][j] == 1):
            print("do Screen.drawPixel(x+",j,", y+",i,");" )

print("white")
for j in range(nW):
    print(" ")
    for i in range(nH):
        if (grid[i][j] == 0):
            print("do Screen.drawPixel(x+",31-j,", y+",i,");" )

im.show()

print(pix[0, 0])
writeToFile(grid)