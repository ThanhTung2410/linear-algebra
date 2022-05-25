# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J4ka_2fDTR3E-wE0i3i5mwdSwf3Xutez
"""

import numpy as np
from sympy import *
from sympy.solvers.solveset import linsolve
from matplotlib import pyplot as plt

print("Câu 1")
print("------------")
list_A = [-12, 3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -11, 12, 371, 153]
vector_A = np.array(list_A)
print("a) Chuyển list thành vector:", vector_A)

print()

matrix_A = vector_A.reshape(3, 5)
print("b) Chuyển véc tơ vừa tạo thành ma trận kích thước 3x5:")
print(matrix_A)

print()

A1 = []
A2 = []

for i in range(0, len(list_A)):
  if (i == 9):
    break
  A1.append(list_A[i])

for i in range(9, len(list_A)):
  if (i == len(list_A)):
    break
  A2.append(list_A[i])

A1 = np.array(A1).reshape(3, 3)
print("Ma trận A1 là:")
print(A1)

print()

A2 = np.array(A2).reshape(3, 2)
print("Ma trận A2 là:")
print(A2)

print()

print("d) Ma trận chuyển vị của ma trận A1:")
print(np.transpose(A1))

print()

print("e) Ma trận nghịch đảo của ma trận A1:")
print(np.linalg.inv(A1))

print()

print("Câu 2")
print("------------")
def isSquare(A):
  dimensionOfMatrix = A.shape # Số chiều của ma trận 
  if(dimensionOfMatrix[0] == dimensionOfMatrix[1]):
    return True
  else:
    return False

def cal_prod_diag(A):
  if (isSquare(A)):
    return A.diagonal().prod()
  else:
    return None

def calculateDet(A):
  if (isSquare(A)):
    return np.linalg.det(A)
  else:
    return None

m = 5
n = 5
A2 = np.random.randint(20, size = (m, n))
print("Ma trận ngẫu nhiên A2 là")
print(A2)
if (isSquare(A2)):
  print("a) Ma trận vuông")
else:
  print("a) Ma trận không vuông")
print("b) Tích các các giá trị nằm trên đường chéo của ma trận vuông:", cal_prod_diag(A2))
print("c) Định thức của ma trận A2 là", calculateDet(A2))

print()

print("Câu 3")
print("------------")
A3 = np.array([ [4 , 5, 6], [1, -1, 0], [0, 1, -1]])
b3 = np.array([[5, 2, 3]]).T
res3_1 = np.linalg.solve(A3, b3)
print("Cách 1")
print("Nghiệm của hpt là", res3_1)

print()

print("Cách 2")
inv_A3 = np.linalg.inv(A3) # ma trận nghịch đảo của ma trận A3
res3_2 = inv_A3.dot(b3)
print("Nghiệm của hpt là", res3_2)

print()

print("Câu 4")
print("------------")
x1, x2, x3, x4, x5 = symbols('x1, x2, x3, x4, x5')
X4 = linsolve([2*x1 - 2*x3, 3*x1 + 4*x2 - 12*x3 - 4*x4 - x5, x2 - 2*x4, x2 - 2*x5, x2 - 3*x3 - x4], (x1, x2, x3, x4, x5))
print("X(x1, x2, x3, x4, x5) =", X4)

print()

print("Câu 5")
print("------------")
A5 = np.array([[-10, 13, 7, -11], [2, 1, -5, 3], [-6, 3, 13, -3], [16, -16, -2, 5], [2, 1, -5, -7]])
print("a) Chuẩn 1 của ma trận A5:", np.linalg.norm(A5, 1))
print("b) Chuẩn Euclide của ma trận A5:", np.linalg.norm(A5, 2))
print("c) Chuẩn vô cùng của ma trận", np.linalg.norm(A5, np.inf))
print("d) chuẩn Frobenius của ma trận", np.linalg.norm(A5, 'fro'))

print()

print("Câu 6")
print("------------")
A6 = np.array([ [3,4,5], [1,3,1], [1,1,2] ])

listUpperCaseChar = list(map(chr, range(97 - 32, 123 - 32)))
listUpperCaseChar.append(" ") # thêm kí tự space

msg = "LINEAR ALGEBRA LABORATORY"

def encodeMessage(msg, encodingMatrix):
  E = [] 
  numbersOfCol = 0
  listCharsOfMsg = list(msg) # convert string to list of characters

  for i in range (0, len(listCharsOfMsg)): # loop through each character of msg
    for j in range (0, len(listUpperCaseChar)): # loop through each character in alphabet
      if listCharsOfMsg[i] == listUpperCaseChar[j]: 
        E.append(j)

  if (len(E) % 3 == 0):
    numberOfCols = int(len(E) / 3)
    E = np.array(E).reshape(3, numberOfCols)
  else:
    while (len(E) % 3 != 0):
      E.append(27) # add character key of space
    numberOfCols = int(len(E) / 3)
    E = np.array(E).reshape(3, numberOfCols)

  msgAfterEncode = encodingMatrix.dot(E)
  return msgAfterEncode.flatten() # convert to 1D array

print("\"LINEAR ALGEBRA LABORATORY\" sau khi mã hóa:",encodeMessage(msg, A6))

print()

print("Câu 7")
print("------------")
A7 = np.array([[-6, 3, -27, -33, -13], [6, -5, 25, 28, 14], [8, -6, 34, 38, 18], [12, -10, 50, 41, 23], [14, -21, 49, 29, 33]])
rank_A7 = np.linalg.matrix_rank(A7)
print("Hạng của ma trận A7 là:", rank_A7)

print()

print("Câu 8")
print("------------")
A8 = np.array([[1, -1], [1, 0], [1, 1], [1, 2]])
b8 = np.array([0 , 1, 2, 4])

transpose_A8 = np.transpose(A8)
transpose_A8_mul_A8 = transpose_A8.dot(A8)
transpose_A8_mul_b8 = transpose_A8.dot(b8)
x8 = np.linalg.solve(transpose_A8_mul_A8, transpose_A8_mul_b8)

x = symbols('x')
y8 = x8[0] + x8[1] * x
print("y =", y8)

# Vẽ đồ thị mô phỏng
x8p = np.arange(-2, 3, 0.01)
y8p = x8[0] + x8[1] * x8p
plt.plot(x8p, y8p, color = 'red')

plt.plot(-1, 0, 'ko',  color = 'green')
plt.plot(0, 1, 'ko',  color = 'green')
plt.plot(1, 2, 'ko',  color = 'green')
plt.plot(2, 4, 'ko',  color = 'green')
plt.show()

print()

print("Câu 9")
print("------------")
A9 = np.array([[-1, 1, 1], [-2, 2, 1], [2, -1, 0]])
eval_A9, evec_A9 = np.linalg.eig(A9)
print("Trị riêng của ma trận A9 là", eval_A9)
print("Vecto riêng của ma trận A9 là:")
print(evec_A9)

print()

print("Câu 10")
print("------------")
A10 = np.array([[2, -1, 1, -6, 8], [1, -2, -4, 3, -2], [-7, 8, 10, 3, -10], [4, -5, -7, 0, 4]])
print("A10=")
print(A10)

print()

U10, S10, V10 = np.linalg.svd(A10)
print("U10=")
print(U10)

print()

print("S10=")
print(S10)

print()

print("V10=")
print(V10)

print()