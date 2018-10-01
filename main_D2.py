'''
Created on Sep 30, 2018

@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X,Y) = X²+Y² 
'''
import numpy as np
import kernel as ker
import matplotlib.pyplot as plt
import timeit


##D2Q9
grid_data_9 = np.zeros(10*10)
output_data_9 = np.zeros(10*10)
rhs_data_9 = np.zeros(10*10)

for i in range(100):
    rhs_data_9[i] = 6
print(rhs_data_9)


##Apply boundary conditions
val_9 = 0
for i in [0,9]:
    for j in range(10):
        val_9=(i+1)*(i+1) + (j+1)*(j+1)
        ker.setDataGhostD2Q9(grid_data_9, i, j, val_9)
for j in [0,9]:
    for i in range(10):
        val_9=(i+1)*(i+1) + (j+1)*(j+1)
        ker.setDataGhostD2Q9(grid_data_9, i, j, val_9)
        

