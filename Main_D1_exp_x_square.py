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
    rhs_array_3[i] = 2 * exp(i*i) *(1 + 2*i*i)




##O(h⁴)
input_array_5=np.zeros(12)

for i in [0, 1, 10, 11]:
    input_array_5[i] = exp(i*i)



output_array_5 = np.copy(input_array_5)

rhs_array_5 = np.zeros(12) 


for i in range(12):
    rhs_array_5[i] = 2 * exp(i*i) *(1 + 2*i*i)


# output_array_3=ker.ExecuteOneJacobiStepD1Q3(input_array_3,output_array_3, rhs_array_3, 2.0/3.0)
# out=ker.ExecuteOneJacobiStepD1Q3(out, rhs_array, 2.0/3.0)




relax = 2/3 

print(input_array_3)
for i in range(500):
    input_array_3 = ker.ExecuteOneJacobiStepD1Q3(input_array_3,output_array_3, rhs_array_3, relax)
    input_array_5 = ker.ExecuteOneJacobiStepD1Q5(input_array_5,output_array_5, rhs_array_5, relax)



#print(output_array_3)
print("d1q3: ",[x for x in output_array_3])
print("d1q5: ",[x for x in output_array_5])






