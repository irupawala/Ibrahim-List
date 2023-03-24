import numpy as np
l = []
def Bersenhams_Circle(matrix, x, y, r):
    i = 0
    j = r
    d = -2 * r + 3
    while i <= j:
        draw(x + i, y + j)
        draw(x + j, y + i)
        draw(x + i, y - j)
        draw(x - j, y + i)
        draw(x - i, y + j)
        draw(x + j, y - i)
        draw(x - i, y - j)
        draw(x - j, y - i)
        if d < 0:
            d += 4*i + 6
            i += 1
        else:
            d += 4*i + 6 - 4*j + 4
            i += 1
            j -= 1

def draw(x, y):
   l.append((x, y))


matrix = [[0 for _ in range(10)] for _ in range(10)]
Bersenhams_Circle(matrix, 4, 4, 3)
for x, y in l:
    #matrix[len(matrix)-1-y][x] = 1
    matrix[x][y] = 1
matrix = np.matrix(matrix)
print(matrix)