'''
Created on Sep 7, 2018

@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X) = X²+Y²+Z² 
'''
import numpy as np
import kernel as ker

def trial_func(val):
    val+=1
    return val
stencill = "d3q7"
grid_data = np.zeros(10*10*10)
output_data = np.zeros(10*10*10)
rhs_data = np.ones(10*10*10)
for i in range(1000):
    rhs_data[i] = 6
# print(rhs_data)

##Boundary Conditions applied
val = 0
for i in [0,9]:
    for j in range(10):
        for k in range(10):
            val =  i*i + j*j + k*k
            grid_data = ker.setDataGhostQ7(grid_data, i, j, k, val)
for j in [0,9]:
    for i in range(10):
        for k in range(10):
            val =  i*i + j*j + k*k
            grid_data = ker.setDataGhostQ7(grid_data, i, j, k, val)
            
for k in [0,9]:
    for j in range(10):
        for i in range(10):
            val =  i*i + j*j + k*k
            grid_data = ker.setDataGhostQ7(grid_data, i, j, k, val)

###

for i in range(100):
    grid_data = ker.ExecuteOneJacobiStepD3Q7(grid_data,rhs_data, 2.0/3.0)# print(output_data)
print("output : ",ker.getDataGhostQ7(grid_data,6,6,6))







