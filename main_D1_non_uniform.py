'''
Created on Sep 7, 2018
# -*- coding: utf-8 -*
@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X) = X² or P(X) = x³
'''
import numpy as np
import matplotlib.pyplot as plt
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
input_array_3 = np.copy(input_array_non_uni)
output_array_non_uni=np.copy(input_array_non_uni)
output_array_3 = np.copy(output_array_non_uni)
rhs_array = np.array([2,2,2,2,2,2,2,2,2,2])

b = np.array([2,2,2,2,2,2,2,-79])
b_5 = np.array([24,24,24,24,24,24,105,-1272])
b_trial = np.array([2,24,24,24,24,24,105,-79])

##O(h⁴)
#input_array_non_uni_5=np.array([1.,4.,0.,0.,0.,0.,0.,0.,0.,0.,121.,144.])

#output_array_non_uni_5 = np.copy(input_array_non_uni_5)

rhs_array_5 = np.array([2,2,2,2,2,2,2,2,2,2,2,2])

dif_non_uni = np.zeros(10)
dif_3 = np.zeros(10)

#output_array_non_uni_5=ker.ExecuteOneJacobiStepD1Q5(output_array_non_uni_5,output_array_non_uni_5, rhs_array_5, 2.0/3.0)
# print(output_array_non_uni_5)
number_of_iter = 300
percent_error_non_uni_through_iterations = np.zeros(number_of_iter)
percent_error_3_through_iterations = np.zeros(number_of_iter)
relax = 2.0/3.0

real_sol =[(x)*(x) for x in range(10)]
for i in range(number_of_iter):
    input_array_non_uni=ker.ExecuteOneJacobiStepD1NonUni(input_array_non_uni,output_array_non_uni, rhs_array, relax)
    input_array_3=ker.ExecuteOneJacobiStepD1Q3(input_array_3,output_array_3, rhs_array, relax)
    for j in range(1,10):
        dif_non_uni[j] = ((abs(output_array_non_uni[j] - real_sol[j]))/real_sol[j]) * 100
        dif_3[j] = ((abs(output_array_3[j] - real_sol[j]))/real_sol[j]) * 100
    percent_error_non_uni = 0
    percent_error_3 = 0
    for j in range(1,10):
        percent_error_non_uni += dif_non_uni[j]
        percent_error_3 += dif_3[j]
    percent_error_non_uni /= 8
    percent_error_3 /= 8
    percent_error_non_uni_through_iterations[i]= percent_error_non_uni
    percent_error_3_through_iterations[i]= percent_error_3
#print(percent_error_3_through_iterations,percent_error_non_uni_through_iterations)
print("d1 non-uni: ",[x for x in output_array_non_uni])
print("d1q3: ",[x for x in output_array_non_uni])


a_range = np.arange(0.,number_of_iter)
plt.plot(a_range,percent_error_3_through_iterations,'-r',label='D1Q3')
plt.plot(a_range,percent_error_non_uni_through_iterations,'-g',label='D1Qnon_uni')
plt.ylabel('percent difference')
plt.xlabel('iteration')
plt.legend()
plt.show()

# print(np.linalg.solve(A,b))
# b = np.linalg.solve(A,b)
#print(np.linalg.solve(A,b))
#print(np.linalg.solve(A_5,b_5))
#print(np.linalg.solve(A_trial,b_trial))
