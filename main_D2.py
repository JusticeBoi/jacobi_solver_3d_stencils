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
rhs_data_9 = np.zeros(10*10)

for i in range(100):
    rhs_data_9[i] = 4
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
        
grid_data_5 = np.copy(grid_data_9)

iter_step = 100
output_data_9 = np.copy(grid_data_9)

output_data_5 = np.copy(grid_data_9) 
ans_array_9_1 = np.zeros(iter_step) 


# ans_array_7_2 = np.zeros(200)
start_9 = timeit.time.perf_counter()

dif_5 = np.zeros(100)
dif_9 = np.zeros(100)
real_sol = [x*x + y*y for x in range(10) for y in range(10)]
percent_error_5_through_iterations = np.zeros(iter_step)
percent_error_9_through_iterations = np.zeros(iter_step)
print(real_sol)
for i in range(iter_step):
    grid_data_9 = ker.ExecuteOneJacobiStepD2Q9(grid_data_9,output_data_9,rhs_data_9, 2.0/3.0)
    grid_data_5 = ker.ExecuteOneJacobiStepD2Q5(grid_data_5,output_data_5,rhs_data_9, 2.0/3.0)
    ans_array_9_1[i]=ker.getDataGhostD2Q9(output_data_9,2,2)
    for j in range(1,100):
        dif_5[j] = ((abs(output_data_5[j] - real_sol[j]))/real_sol[j]) * 100
        dif_9[j] = ((abs(output_data_9[j] - real_sol[j]))/real_sol[j]) * 100
    percent_error_5 = 0
    percent_error_9 = 0
    for j in range(1,100):
        percent_error_5 += dif_5[j]
        percent_error_9 += dif_9[j]
    percent_error_5 /= 64
    percent_error_9 /= 64
    percent_error_5_through_iterations[i]= percent_error_5
    percent_error_9_through_iterations[i]= percent_error_9

#     ans_array_7_2[i]=ker.getDataGhostQ7(output_data_7,6,6,6)
end_9 =timeit.time.perf_counter()
time_9 = end_9-start_9
#for i in range(iter_step):
#    print("output 9 {:d} iteration x,y,z = 2, 2, 2 : ".format(i),ans_array_9_1[i])
print("outputdata 9 : ",output_data_9)
print("outputdata 5 : ",output_data_5)


a_range = np.arange(0.,iter_step)
plt.plot(a_range,percent_error_5_through_iterations,'-r',label='D2Q5')
plt.plot(a_range,percent_error_9_through_iterations,'-g',label='D2Q9')
plt.ylabel('average percent difference')
plt.xlabel('iteration')
plt.legend()
plt.semilogx()
plt.show()
