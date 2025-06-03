def MainDiag(mat, n):
    for i in range(n):
        for j in range(i + 1, n):
            if mat[i][j] != mat[j][i]:
                return False
    return True

def MinorDiag(mat, n):
    for i in range(n):
        for j in range(i+1):
          if mat[i][j] != mat[n-j-1][n-i-1]:
             return False
    #         if mat[i][j] == mat[n - i][n - j]:
    # if mat[n-1][0] == mat[1][n]:
    #   if mat[n][0] == mat[0][n]:
    #     if mat[n][1] == mat[0][n-1]:
          # return True
    return True

# def MinorDiag(mat, n):
#     if mat[n - 1][0] == mat[0][n - 1]:
#       if mat[n][0] == mat[1][n]:
#         return True
#     return False

def VertAxis(mat, n):
    for i in range(n):
        for j in range(n // 2):
            if mat[i][j] != mat[i][n - j - 1]:
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
      row.append(number)
    input.append(row)
    l += 1
    if l == k:
       break
      

# n = [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
m = len(input)

a = MainDiag(input, m)
b = MinorDiag(input, m)
c = VertAxis(input, m)
output_list = [a, b, c]

output=""
for i in output_list:
  if (i == True):
    output += "1 "
  else:
    output += "0 "

output = output[:len(output)-1]
print(output)
