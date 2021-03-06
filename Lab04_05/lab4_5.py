# -*- coding: utf-8 -*-
"""Lab4_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_W3ggXErywF9UczRhqVm61yOwg7q9Swp

Exercise 1: Find the solution of the linear systems
"""

import numpy as np

# a)
A1a = np.array([ [1,2,1], [2,-1,1], [2,1,0]])
b1a = np.array([[0, 0, 0]]).T
result1a = np.linalg.solve(A1a, b1a)
print("a) Nghiệm của hpt là:")
print(result1a)

print()

# b)
A1b = np.array([ [2,1,1,1], [1,2,1,1], [1,1,2,2], [1,1,1,2]])
b1b = np.array([[1,1,1,1]]).T
result1b = np.linalg.solve(A1b, b1b)
print("b) Nghiệm của hpt là:")
print(result1b)

"""Exercise 2: Consider the following system of linear equations:"""

import numpy as np 
from matplotlib import pyplot as plt

# (a) The system has no solutions.
x2a = np.arange(-5, 0, 0.05)
y2a1 = -x2a - 1
y2a2 = -x2a - 2
plt.title("a) The system has no solutions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x2a, y2a1)
plt.plot(x2a, y2a2)
plt.show()

print()

# (b) The system has a unique solution.
"""
4x + 3y = -6
5x + 8y = 1
x + y = -1
Giải ra nghiệm (x = -3, y = 2)
"""

x2b = np.arange(-5, 0, 0.05)
y2b1 = -x2b - 1
y2b2 = (1 - 5*x2b) / 8
y2b3 = (-6 - 4*x2b) / 3

plt.title("b) The system has a unique solution")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x2b, y2b1)
plt.plot(x2b, y2b2)
plt.plot(x2b, y2b3)
plt.show()

print()

# (c) The system has infinitely many solutions.
x2c = np.arange(-5, 0, 0.05)
y2c1 = -x2c - 1
y2c2 = -x2c - 1
plt.title("c) The system has infinitely many solutions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x2c, y2c1)
plt.plot(x2c, y2c2)
plt.show()

"""Exercise 3: Consider the following system of linear equations"""

import numpy as np 
from numpy.linalg import matrix_rank

def solveLinearEquation(A, b, A_b):
    if (matrix_rank(A) == matrix_rank(A_b) and matrix_rank(A) == len(A[0]) and matrix_rank(A_b) == len(A[0])):
      print("The system has a unique solution", np.linalg.solve(A, b.T))
    elif (matrix_rank(A) == matrix_rank(A_b) and matrix_rank(A) < len(A[0]) and matrix_rank(A_b) < len(A[0])):
      print("The system has infinitely many solutions")
    elif (matrix_rank(A) != matrix_rank(A_b)):
      print("The system has no solutions")

# (a) The system has no solutions.
A3a = np.array([ [1, 6, 4], [8, -5, 8], [6, -17, 0] ])
b3a = np.array([9,24,24])
A3a_b3a = np.array([ [1, 6, 4, 9], [8, -5, 8, 24], [6, -17, 0, 24] ])
solveLinearEquation(A3a, b3a, A3a_b3a)

print()

# (b) The system has a unique solution.
A3b = np.array([ [1, 6, 4], [1, -5, 3], [2, 1, 7] ])
b3b = np.array([9,24,33])
A3b_b3b = np.array([ [1, 6, 4, 9], [1, -5, 3, 24], [2, 1, 7, 33] ])
solveLinearEquation(A3b, b3b, A3b_b3b)

print()

# (c) The system has infinitely many solutions.
A3c = np.array([ [2, 1, -2], [3, 2, 2], [5, 4, 3] ])
b3c = np.array([10,1,4])
A3c_b3c = np.array([ [2, 1, -2, 10], [3, 2, 2, 1], [5, 4, 3, 4] ])
solveLinearEquation(A3c, b3c, A3c_b3c)

"""Exercise 4:"""

import numpy as np 

# a)
A4 = np.array([ [1,1,2], [3,6,-5], [2,4,-3]])
detA4 = np.linalg.det(A4)
print("det(A) =", detA4)
if (detA4 != 0):
  print("a) A is invertible")
else:
  print("a) A isn't invertible")

print()

# b)
b4 = np.array([1, -1, 0])
inv_A4 = np.linalg.inv(A4) # ma trận nghịch đảo của ma trận A
result = inv_A4.dot(b4)
print("b) Nghiệm của hpt là")
print(result)

"""Exercise 5: Try to use the three different methods to solve the following system:"""

import numpy as np

# Cách 1
A5 = np.array([ [1,2,1], [2,2,2], [2,4,1] ])
b5 = np.array([ [1, 1, 2] ]).T
result1 = np.linalg.solve(A5, b5)
print("Cách 1: Nghiệm của hpt là")
print(result1)

print()

# Cách 2
inv_A5 = np.linalg.inv(A5) # ma trận nghịch đảo của ma trận A
result2 = inv_A5.dot(b5)
print("Cách 2: Nghiệm của hpt là")
print(result2)

print()

# Cách 3
A51 = np.array([ [1,2,1], [1,2,2], [2,4,1]])
A52 = np.array([ [1,1,1], [2,1,2], [2,2,1]])
A53 = np.array([ [1,2,1], [2,2,1], [2,4,2]])
detA5 = np.linalg.det(A5)
detA51 = np.linalg.det(A51)
detA52 = np.linalg.det(A52)
detA53 = np.linalg.det(A53)
print("Cách 3: x, y, z =", detA51/detA5, detA52/detA5, detA53/detA5)

"""Exercise 6: Find the interpolating polynomial p(t) = a0 + a1 t + a2 t**2
for the data (1,6), (2,15), (3,38). That is, find a0, a1 and a2
"""

import numpy as np
A6 = np.array([ [1,1,1], [1,2,4], [1,3,9] ])
b6 = np.array([6,15,38]).T
result = np.linalg.solve(A6, b6)
print("a0, a1, a2 lần lượt =", result)

"""Exercise 7: A group took a trip on a bus, at 3 per child and 3.2 per adult for a total of 118.4. They took the train back at 3.5 per child and 3.6 per adult for a total of 135.2. How many children and how many adults?"""

import numpy as np
A7 = np.array([ [3,3.2], [3.5,3.6]])
b = np.array([118.4,135.2]).T
result = np.linalg.solve(A7, b)
print("Vậy số trẻ nhỏ và số người lớn lần lượt là:", result)

"""Exercise 8: Global positioning system (GPS) is used to find our location. Satellites send signals to a receiver on earth with information about the location of the satellite in xyz-coordinate system and the time t when the signal was transmitted. After some calculations we obtain the following three linear equations. Solve these equations."""

from sympy import *
from sympy.solvers.solveset import linsolve
x, y, z, t = symbols('x, y, z, t')
X8 = linsolve([2*x - 4*y + 4*z + 0.077*t - 3.86, -2*y + 2*z - 0.056*t + 3.47, 2*x - 2*y], (x, y, z, t))
print("X8 =", X8)

"""Exercise 9: The actual color a viewer sees on a screen is influenced by the specific type and amount of phosphors on the the screen. So each computer screen manufacturer must convert between the (R,G,B) data and an international CIE standard for color, which uses three primary colors, called X, Y, and Z.
A typical conversion for short-persistence phosphors is
"""

from sympy import *
import numpy as np
x, y, z = symbols('x, y, z')
A9 = np.array([ [0.61, 0.29, 0.15], [0.35, 0.59, 0.063], [0.04, 0.12, 0.787] ])
# CIE(x, y, z) => RGB(R, G, B)
x = 1
y = 1
z = 1.5
b9 = np.array([x,y,z])
b9t = np.transpose(b9)
RGB = np.linalg.solve(A9, b9t)
print("RGB =", RGB)

"""Exercise 10: The Leontief model represents the economy as a linear system. Consider a particular economy which depends on oil (O), energy (E) and services (S). the input-output matrix A of such an economy is given by"""

import numpy as np
A10 = np.array([ [0.25,0.15,0.1], [0.4,0.15,0.2], [0.15,0.2,0.2]])
I3 = np.array([ [1,0,0], [0,1,0], [0,0,1]])
# p = Ap + d
# => p = [(I3 - A)^(-1)] * d
d10 = np.array([100,100,100]).T
p10 = np.linalg.inv(I3 - A10).dot(d10)
print("p10 =", p10)

"""Exercise 11: Chemical equations describe the quantities of substances consumed and produced by chemical reactions."""

# (x1)C3H8 + (x2)O2 -> (x3)C02 + (x4)H2O
# C: 3*x1 = x3 => 3*x1 - x3 = 0
# H: 8*x1 = 2*x4 => 8*x1 - 2*x4 = 0
# O: 2*x2 = 2*x3 + x4 => 2*x2 - 2*x3 - x4 = 0

from sympy import *
from sympy.solvers.solveset import linsolve
x1, x2, x3, x4 = symbols('x1, x2, x3, x4')
X = linsolve([3*x1 - x3, 8*x1 - 2*x4, 2*x2 - 2*x3 - x4], (x1, x2, x3, x4))
print("X(x1, x2, x3, x4) =", X)
# x4 = 4 => x1 = x4/4 = 1; x2 = 5x4/4 = 5; x3 = 3x4/4 = 3; x4=4
# C3H8 + 5O2 -> 3CO2 + 4H2O

print()
# (y1)KMnO4 -> (y2)MnO2 + (y3)O2 + (y4)K2MnO4
# K: y1 = 2*y4 => y1 - 2*y4 = 0
# Mn: y1 = y2 + y4 => y1 - y2 - y4 = 0
# O: 4*y1 = 2*y2 + 2*y3 + 4*y4 => 4*y1 - 2*y2 - 2*y3 - 4*y4 = 0
y1 ,y2 ,y3 ,y4 = symbols('y1, y2, y3, y4')
Y = linsolve([y1 - 2*y4, y1 - y2 - y4, 4*y1 - 2*y2 - 2*y3 - 4*y4], (y1, y2, y3, y4))
print("Y(y1, y2, y3, y4) =", Y)

"""Exercise 12: In the following puzzle the row and columns add up to the numbers which are in the bold font. Find all the unknown x's"""

from sympy import * 
from sympy.solvers.solveset import linsolve
# x1 + x2 + x3 = 15
# x4 + x5 + x6 = 6
# x1 + x4 = 8
# x2 + x5 = 7
# x3 + x6 = 6
x1, x2, x3, x4, x5, x6, s, t = symbols('x1, x2, x3, x4, x5, x6, s, t')
x5 = s
x6 = t
X12 = linsolve([x1 + x2 + x3 - 15, x4 + x5 + x6 - 6, x1 + x4 - 8, x2 + x5 - 7, x3 + x6 - 6], (x1, x2, x3, x4, x5, x6))
print("X(x1, x2, x3, x4, x5, x6) =", X12)
# Solution: x1 = 2 + s + t, x2 = 7 - s, x3 = 6 - t, x4 = 6 - s - t, x5 = s, x6 = t
# Nếu s = 1, t = 1 => x1 = 4, x2 = 6, x3 = 5, x4 = 4