'''
Created on Sep 7, 2018

@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X)=e**(x**2)
'''
import numpy as np
import kernel as ker
from math import exp 
def change(ar):
    ar[0] =100

input_array_3 = np.zeros(10)
##boundary conditions
for i in [0,9]:
    input_array_3[i] = exp(i*i)




output_array_3=np.copy(input_array_3)

rhs_array_3 = np.zeros(10)

for i in range(10):
    rhs_array_3 = 2 * exp(i*i) * (1 + 2*x*x )




##O(h⁴)
input_array_5=np.array([1.,4.,0.,0.,0.,0.,0.,0.,0.,0.,121.,144.])
input_array_5_cube  = np.zeros(12)
input_array_5_large = np.zeros(102)
for i in [0,1,10,11]:
    input_array_5_cube[i] = pow(i,3)

for i in [0,1,100,101]:
    input_array_5_large[i] = (i+1)*(i+1)    

output_array_5_cube = np.zeros(12)

output_array_5_large = np.zeros(102)

output_array_5 = np.copy(input_array_5)

output_array_5_cube = np.copy(input_array_5_cube)
output_array_5_large = np.copy(input_array_5_large)
rhs_array_5 = np.array([2,2,2,2,2,2,2,2,2,2,2,2])

rhs_array_5_cube = np.zeros(12)
rhs_array_5_large = np.zeros(102)
for i in range(12):
    rhs_array_5_cube[i] = 6 * i

for i in range(102):
    rhs_array_5_large[i] = 2     


# output_array_3=ker.ExecuteOneJacobiStepD1Q3(input_array_3,output_array_3, rhs_array_3, 2.0/3.0)
# out=ker.ExecuteOneJacobiStepD1Q3(out, rhs_array, 2.0/3.0)


output_array_5=ker.ExecuteOneJacobiStepD1Q5(output_array_5,output_array_5, rhs_array_5, 2.0/3.0)
# print(output_array_5)
# a_np_array = np.array([1,2,3])
# change(a_np_array)
# print(a_np_array)
relax = 2/3 
##input_array_3
for i in range(300):
#     input_array_3=ker.ExecuteOneJacobiStepD1Q3(input_array_3,output_array_3, rhs_array_3, relax)
#     input_array_3_large=ker.ExecuteOneJacobiStepD1Q3Large(input_array_3_large,output_array_3_large, rhs_array_3_large, relax)
    input_array_3_cube=ker.ExecuteOneJacobiStepD1Q3(output_array_3_cube,output_array_3_cube, rhs_array_3_cube, relax)
#     input_array_5=ker.ExecuteOneJacobiStepD1Q5(input_array_5,output_array_5, rhs_array_5, relax)
    input_array_5_cube=ker.ExecuteOneJacobiStepD1Q5(input_array_5_cube,output_array_5_cube, rhs_array_5_cube, relax)      
#     input_array_5_large=ker.ExecuteOneJacobiStepD1Q5Large(input_array_5_large,output_array_5_large, rhs_array_5_large, relax)
# print(output_array_3)
# print("d1q3: ",[x for x in output_array_3[1:-1]])
# print("d1q3 large: ",[x for x in output_array_3_large])
# print("d1q3: ",[x for x in output_array_3[1:-1]])
print("d1q3 cube: ",[x for x in output_array_3_cube])
# print("d1q5: ",[x for x in output_array_5[2:-2]])
# print("d1q5 large: ",[x for x in output_array_5_large])
print("d1q5 cube : ",[x for x in output_array_5_cube])
# print(np.linalg.solve(A,b))
# b = np.linalg.solve(A,b)
# print(np.linalg.solve(A,b))
# print(np.linalg.solve(A_5,b_5))
