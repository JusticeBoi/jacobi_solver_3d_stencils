'''
Created on Sep 7, 2018

@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X) = X²+Y²+Z² 
'''
import numpy as np
import kernel as ker
import matplotlib.pyplot as plt
import timeit

###D3Q7 setting start
grid_data_7 = np.zeros(10*10*10)
output_data_7 = np.zeros(10*10*10)
rhs_data_7 = np.ones(10*10*10)
for i in range(1000):
    rhs_data_7[i] = 6
# print(rhs_data)

##Boundary Conditions applied
val_7 = 0
for i in [0,9]:
    for j in range(10):
        for k in range(10):
            val_7 =  i*i + j*j + k*k
            grid_data_7 = ker.setDataGhostQ7(grid_data_7, i, j, k, val_7)
for j in [0,9]:
    for i in range(10):
        for k in range(10):
            val_7 =  i*i + j*j + k*k
            grid_data_7 = ker.setDataGhostQ7(grid_data_7, i, j, k, val_7)
            
for k in [0,9]:
    for j in range(10):
        for i in range(10):
            val_7 =  i*i + j*j + k*k
            grid_data_7 = ker.setDataGhostQ7(grid_data_7, i, j, k, val_7)

###
output_data_7 = np.copy(grid_data_7)
ans_array_7 = np.zeros(100)
start_7 = timeit.time.perf_counter()
for i in range(100):
    output_data_7 = ker.ExecuteOneJacobiStepD3Q7(output_data_7,output_data_7,rhs_data_7, 2.0/3.0)
    ans_array_7[i]=ker.getDataGhostQ7(output_data_7,2,2,2)
end_7 =timeit.time.perf_counter()
time_7 = end_7-start_7
print("output 7 : ",ker.getDataGhostQ7(output_data_7,2,2,2))
###D3Q7 setting end

###D3Q13 setting start
grid_data_13 = np.zeros(12*12*12)
output_data_13 = np.zeros(12*12*12)
rhs_data_13 = np.ones(12*12*12)
for i in range(12*12*12):
    rhs_data_13[i] = 6
val_13 = 0
for i in [0,1,10,11]:
    for j in range(12):
        for k in range(12):
            val_13 =  i*i + j*j + k*k
            grid_data_13 = ker.setDataGhostQ13(grid_data_13, i, j, k, val_13)
for j in [0,1,10,11]:
    for i in range(12):
        for k in range(12):
            val_13 =  i*i + j*j + k*k
            grid_data_13 = ker.setDataGhostQ13(grid_data_13, i, j, k, val_13)
            
for k in [0,1,10,11]:
    for j in range(12):
        for i in range(12):
            val_13 =  i*i + j*j + k*k
            grid_data_13 = ker.setDataGhostQ13(grid_data_13, i, j, k, val_13)

output_data_13 = np.copy(grid_data_13)
ans_array_13 = np.zeros(100)
start_13 = timeit.time.perf_counter()
for i in range(100):
    output_data_13 = ker.ExecuteOneJacobiStepD3Q13(output_data_13,output_data_13,rhs_data_13, 2.0/3.0)
    ans_array_13[i] =ker.getDataGhostQ13(output_data_13,2,2,2)
end_13 =timeit.time.perf_counter()
time_13 = end_13-start_13
# output_data_13 = ker.ExecuteOneJacobiStepD3Q13(grid_data_13,output_data_13,rhs_data_13, 2.0/3.0)


print("output 13 : ",ker.getDataGhostQ13(output_data_13,2,2,2))


difference = np.empty(100)

for i in range(100):
    difference[i] = ans_array_13[i] - ans_array_7[i]

a_range = np.arange(0.,100.,1.)
true_val = np.empty(100)
true_val.fill(12)

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(a_range,ans_array_7,'r--',label='D3Q7')
ax1.plot(a_range,ans_array_13,'g^',label='D3Q13')
ax1.plot(a_range,true_val,label='True Solution')
plt.ylabel('value')
plt.xlabel('iteration')
plt.title('Poisson Equation')
plt.legend()


ax2 = fig.add_subplot(212)
ax2.plot(a_range,difference,label='Diff. Between 7 and 13')
plt.ylabel('difference')
plt.xlabel('iteration')
plt.legend()
plt.show()

# print("time_7 : ",time_7," time_13: ",time_13)