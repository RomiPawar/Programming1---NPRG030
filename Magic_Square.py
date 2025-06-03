import math

def MM(matrix):
    n = len(matrix)
    diagsum1 = 0
    diagsum2 = 0
    for i in range(n):
        diagsum1 += matrix[i][i]
        diagsum2 += matrix[i][n - i - 1]
    if not (diagsum1 == diagsum2):
        return False
    for i in range(n):
        rowsum = 0
        colsum = 0
        for j in range(n):
            rowsum += matrix[i][j]
            colsum += matrix[j][i]
        if not (rowsum == colsum == diagsum1):
            return False
    return True

def MM2(matrix, zrow, zcol, sum_value):
    n = len(matrix)
    for row in range(n):
        if row != zrow:
            if sum(input[row]) != sum_value:
                return False
    for col in range(n):
        if col != zcol:
            s = 0
            for i in range(n):
                s += matrix[i][col]
            if s != sum_value:
                return False
    diagsum1 = 0
    diagsum2 = 0
    for i in range(n):
        diagsum1 += matrix[i][i]
        diagsum2 += matrix[i][n - i - 1]
    if diagsum1 != sum_value:
        return False
    if diagsum2 != sum_value:
        return False
    return True

import sys
# for line in sys.stdin:
#   row = list(map(int, line.split()))

input = []
l = 0
for line in sys.stdin:
    row = []
    k = len(line.split())
    for number in line.split():
      row.append(int(number))
    input.append(row)
    l += 1
    if l == k:
       break

zrow, zcol = None, None
for row in range(l):
    for col in range(l):
        if input[row][col] == 0:
            zrow, zcol = row, col
            break
    if zrow is not None:
        break

sum_value = 0
for row in range(l):
    if row != zrow:
        for col in range(l):
            sum_value += input[row][col]
        break


# mnum = l * (l ** 2 + 1) // 2
# znum = mnum - sum(input[zrow])
znum = sum_value - sum(input[zrow])
input[zrow][zcol] = znum


if MM2(input, zrow, zcol, sum_value):
    # print("Magic Square")
    for row in input:
        print(" ".join(str(cell) for cell in row))

else:
    print("Can't be magic")
