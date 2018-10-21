'''
Created on Sep 7, 2018
# -*- coding: utf-8 -*
@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X) = X² or P(X) = x³
'''
import numpy as np
import kernel_non_uniform as ker
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
input_array_non_uni=np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,81.])
input_array_non_uni_3 = np.copy(input_array_non_uni)
output_array_non_uni=np.copy(input_array_non_uni)
output_array_non_uni_3 = np.copy(output_array_non_uni)
rhs_array = np.array([2,2,2,2,2,2,2,2,2,2])

b = np.array([2,2,2,2,2,2,2,-79])
b_5 = np.array([24,24,24,24,24,24,105,-1272])
b_trial = np.array([2,24,24,24,24,24,105,-79])

##O(h⁴)
input_array_non_uni_5=np.array([1.,4.,0.,0.,0.,0.,0.,0.,0.,0.,121.,144.])

output_array_non_uni_5 = np.copy(input_array_non_uni_5)

rhs_array_5 = np.array([2,2,2,2,2,2,2,2,2,2,2,2])
#output_array_non_uni_5=ker.ExecuteOneJacobiStepD1Q5(output_array_non_uni_5,output_array_non_uni_5, rhs_array_5, 2.0/3.0)
# print(output_array_non_uni_5)
relax = 2.0/3.0
for i in range(200):
     input_array_non_uni=ker.ExecuteOneJacobiStepD1NonUni(input_array_non_uni,output_array_non_uni, rhs_array, relax)
     input_array_non_uni_3=ker.ExecuteOneJacobiStepD1Q3(input_array_non_uni_3,output_array_non_uni_3, rhs_array, relax)

print("d1 non-uni: ",[x for x in output_array_non_uni])
print("d1q3: ",[x for x in output_array_non_uni_3])
# print(np.linalg.solve(A,b))
# b = np.linalg.solve(A,b)
print(np.linalg.solve(A,b))
#print(np.linalg.solve(A_5,b_5))
print(np.linalg.solve(A_trial,b_trial))
