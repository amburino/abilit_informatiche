l = []
with open('input1.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0:
     l.append(list(map(int, line.split(','))))
#print(l)
#################

lettura= open("input1.txt", "r")
a=[]
for line in lettura.readlines():
  a.append([int(x) for x in line.split(',')])
#print(a)
##################

import math

# 3x3 matrix
X = [[12,7,3],[4 ,5,6],[7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],[6,7,3,0],[4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(X)):
  for j in range(len(Y[0])):
    for k in range(len(Y)):
      result[i][j] += X[i][k] * Y[k][j]
for r in result:
  print(r)
print("----------")
result1= [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
for r in result:
  print(r)

########################
print("----------")
#matrix x scalar showing AxB != BxA
A = [[12,7,3],[4 ,5,6],[7 ,8,9]]
# 3x4 matrix
B = [[5,8,1,2],[6,7,3,0],[4,5,9,1]]
def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):   
      print(str((matrix[i][j]))+"\t", end='')
    print("\n")
def matrix_x_matrix(X, Y):
 result= [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
 for i in range(len(X)):
   for j in range(len(Y[0])):
     for k in range(len(Y)):
       result[i][j] += X[i][k] * Y[k][j]
 return result
print_matrix(matrix_x_matrix(A,B))
print("------")
print_matrix(matrix_x_matrix(B,A))