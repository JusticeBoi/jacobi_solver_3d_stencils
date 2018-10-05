'''
Created on Sep 30, 2018

@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X,Y) = X²+Y² or P(X,Y) = e⁽2x+2y⁾
'''
import numpy as np
import kernel as ker
import matplotlib.pyplot as plt
import timeit
from math import exp 


##D2Q9
grid_data_9 = np.zeros(10*10)
output_data_9 = np.zeros(10*10)
grid_data_9_exp = np.zeros(10*10)
output_data_9_exp = np.zeros(10*10)
rhs_data_9 = np.zeros(10*10)
rhs_data_9_exp = np.zeros(10*10)

for i in range(100):
    rhs_data_9[i] = 4
    
for i in range(10):
    for j in range(10):
        rhs_data_9_exp[10*i + j] = (8.0)*exp(2*i + 2*j)
        
# print(rhs_data_9_exp)
##Apply boundary conditions
val_9 = 0
for i in [0,9]:
    for j in range(10):
        val_9=(i)*(i) + (j)*(j)
        ker.setDataGhostD2Q9(grid_data_9, i, j, val_9)
for j in [0,9]:
    for i in range(10):
        val_9=(i)*(i) + (j)*(j)
        ker.setDataGhostD2Q9(grid_data_9, i, j, val_9)
        
val_9_exp = 0
for i in [0,9]:
    for j in range(10):
        val_9_exp=exp(2*i + 2*j)
        ker.setDataGhostD2Q9(grid_data_9_exp, i, j, val_9_exp)
for j in [0,9]:
    for i in range(10):
        val_9_exp=exp(2*i + 2*j)
        ker.setDataGhostD2Q9(grid_data_9_exp, i, j, val_9_exp)
        
# print(grid_data_9_exp)
iter_step = 100
output_data_9 = np.copy(grid_data_9)
ans_array_9_1 = np.zeros(iter_step) 

output_data_9_exp = np.copy(grid_data_9_exp)
ans_array_9_1_exp = np.zeros(iter_step)

# ans_array_7_2 = np.zeros(200)
start_9 = timeit.time.perf_counter()


for i in range(iter_step):
    output_data_9 = ker.ExecuteOneJacobiStepD2Q9(output_data_9,output_data_9,rhs_data_9, 2.0/3.0)
    ans_array_9_1[i]=ker.getDataGhostD2Q9(output_data_9,2,2)
    
    output_data_9_exp = ker.ExecuteOneJacobiStepD2Q9(output_data_9_exp,output_data_9_exp,rhs_data_9_exp, 2.0/3.0)
    ans_array_9_1_exp[i]=ker.getDataGhostD2Q9(output_data_9_exp,1,1)
#     ans_array_7_2[i]=ker.getDataGhostQ7(output_data_7,6,6,6)
end_9 =timeit.time.perf_counter()
time_9 = end_9-start_9
for i in range(iter_step):
    print("output 9 {:d} iteration x,y,z = 2, 2, 2 : ".format(i),ans_array_9_1[i])
#     print("output 9 exp {:d} iteration x,y,z = 1, 1, 1 : ".format(i),ans_array_9_1_exp[i])

