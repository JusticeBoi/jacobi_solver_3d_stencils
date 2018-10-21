'''
Created on Sep 7, 2018
# -*- coding: utf-8 -*
@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X) = X² or P(X) = x³
'''
import numpy as np
import kernel_high_order as ker
from math import exp
def change(ar):
    ar[0] =100
A = np.array([[-2,1,0,0,0,0,0,0],
              [1,-2,1,0,0,0,0,0],
              [0,1,-2,1,0,0,0,0],
              [0,0,1,-2,1,0,0,0],
              [0,0,0,1,-2,1,0,0],
              [0,0,0,0,1,-2,1,0],
              [0,0,0,0,0,1,-2,1],
              [0,0,0,0,0,0,1,-2]])
A_5 = np.array([[-30,16,-1,0,0,0,0,0],
              [16,-30,16,-1,0,0,0,0],
              [-1,16,-30,16,-1,0,0,0],
              [0,-1,16,-30,16,-1,0,0],
              [0,0,-1,16,-30,16,-1,0],
              [0,0,0,-1,16,-30,16,-1],
              [0,0,0,0,-1,16,-30,16],
              [0,0,0,0,0,-1,16,-30]])

A_trial = np.array([[-2,1,0,0,0,0,0,0],
              [16,-30,16,-1,0,0,0,0],
              [-1,16,-30,16,-1,0,0,0],
              [0,-1,16,-30,16,-1,0,0],
              [0,0,-1,16,-30,16,-1,0],
              [0,0,0,-1,16,-30,16,-1],
              [0,0,0,0,-1,16,-30,16],
              [0,0,0,0,0,0,1,-2]])
##O(h²)
input_array_3 = np.array([1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,144.])
input_array_5 = np.array([1.,4.,0.,0.,0.,0.,0.,0.,0.,0.,121.,144.])

output_array_3 = np.copy(input_array_3)
rhs_array_3 = np.array([2,2,2,2,2,2,2,2,2,2,2,2])

output_array_5 = np.copy(input_array_5)
rhs_array_5 = np.array([2,2,2,2,2,2,2,2,2,2,2,2])

b = np.array([2,2,2,2,2,2,2,-79])
b_5 = np.array([24,24,24,24,24,24,105,-1272])
b_trial = np.array([2,24,24,24,24,24,105,-79])

relax = 2.0/3.0
for i in range(200):
     input_array_3=ker.ExecuteOneJacobiStepD1Q3(input_array_3,output_array_3, rhs_array_3, relax)
     input_array_5=ker.ExecuteOneJacobiStepD1Q5(input_array_5,output_array_5, rhs_array_5, relax)

print("d1q3 : ",[x for x in output_array_3])
print("d1q5 : ",[x for x in output_array_5])
# print(np.linalg.solve(A,b))
# b = np.linalg.solve(A,b)
print(np.linalg.solve(A,b))
#print(np.linalg.solve(A_5,b_5))
print(np.linalg.solve(A_trial,b_trial))
