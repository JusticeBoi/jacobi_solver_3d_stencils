'''
Created on Sep 7, 2018

@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X,Y,Z) = X²+Y²+Z²

'''

import timeit
import matplotlib.pyplot as plt
import numpy as np
import kernel as ker
number_of_iter = 50
###D3Q7 setting start
grid_data_7 = np.zeros(10*10*10)
output_data_7 = np.zeros(10*10*10)
rhs_data_7 = np.ones(10*10*10)
for i in range(1000):
    rhs_data_7[i] = 6
# print(rhs_data)

output_array_7 = np.zeros(shape=(number_of_iter,1000))
output_array_13 = np.zeros(shape=(number_of_iter,1000))
##Boundary Conditions applied
val_7 = 0
for i in [0,9]:
    for j in range(10):
        for k in range(10):
            val_7 =  (i)*(i) + (j)*(j) + (k)*(k)
            grid_data_7 = ker.setDataGhostQ7(grid_data_7, i, j, k, val_7)
for j in [0,9]:
    for i in range(10):
        for k in range(10):
            val_7 =  (i)*(i) + (j)*(j) + (k)*(k)
            grid_data_7 = ker.setDataGhostQ7(grid_data_7, i, j, k, val_7)
for k in [0,9]:
    for j in range(10):
        for i in range(10):
            val_7 =  (i)*(i) + (j)*(j) + (k)*(k)
            grid_data_7 = ker.setDataGhostQ7(grid_data_7, i, j, k, val_7)
print(grid_data_7)

###
output_data_7 = np.copy(grid_data_7)
ans_array_7_1 = np.zeros(number_of_iter)
ans_array_7_2 = np.zeros(number_of_iter)
ans_array_7_3 = np.zeros(number_of_iter)
start_7 = timeit.time.perf_counter()
for i in range(number_of_iter):
    grid_data_7 = ker.ExecuteOneJacobiStepD3Q7(grid_data_7,output_data_7,rhs_data_7, 2.0/3.0)
    ans_array_7_1[i]=ker.getDataGhostQ7(output_data_7,2,2,2)
    ans_array_7_2[i]=ker.getDataGhostQ7(output_data_7,6,6,6)
    ans_array_7_3[i]=ker.getDataGhostQ7(output_data_7,3,3,3)
    output_array_7[i] = output_data_7


end_7 =timeit.time.perf_counter()
time_7 = end_7-start_7

iter_range = np.arange(1,number_of_iter,25)

###D3Q7 setting end

###D3Q13 setting start
grid_data_13 = np.zeros(10*10*10)
output_data_13 = np.zeros(10*10*10)
rhs_data_13 = np.ones(10*10*10)
for i in range(10*10*10):
    rhs_data_13[i] = 6
val_13 = 0
for i in [0, 1,8,9]:
    for j in range(10):
        for k in range(10):
            val_13 =  i*i + j*j + k*k
            grid_data_13 = ker.setDataGhostQ7(grid_data_13, i, j, k, val_13)
for j in [0, 1, 8, 9]:
    for i in range(10):
        for k in range(10):
            val_13 =  i*i + j*j + k*k
            grid_data_13 = ker.setDataGhostQ7(grid_data_13, i, j, k, val_13)
for k in [0,1,8,9]:
    for j in range(10):
        for i in range(10):
            val_13 =  i*i + j*j + k*k
            grid_data_13 = ker.setDataGhostQ7(grid_data_13, i, j, k, val_13)

output_data_13 = np.copy(grid_data_13)
ans_array_13_1 = np.zeros(number_of_iter)
ans_array_13_2 = np.zeros(number_of_iter)
ans_array_13_3 = np.zeros(number_of_iter)


start_13 = timeit.time.perf_counter()
for i in range(number_of_iter):
    grid_data_13 = ker.ExecuteOneJacobiStepD3Q13(grid_data_13,output_data_13,rhs_data_13, 2.0/3.0)
    ans_array_13_1[i] =ker.getDataGhostQ13(output_data_13,2,2,2)
    ans_array_13_2[i] = ker.getDataGhostQ13(output_data_13,6,6,6)
    ans_array_13_3[i] = ker.getDataGhostQ13(output_data_13,3,3,3)
    output_array_13[i] = output_data_13

#print(ans_array_7_1,ans_array_13_1)
#print(ans_array_7_3[50], ans_array_13_3[50]  )
end_13 =timeit.time.perf_counter()
time_13 = end_13-start_13
# output_data_13 = ker.ExecuteOneJacobiStepD3Q13(grid_data_13,output_data_13,rhs_data_13, 2.0/3.0)


#for i in iter_range:
#    print("output 7 {:d} iteration x,y,z = 5, 5, 5 : ".format(i),ans_array_7_1[i])
#for i in iter_range:
#    print("output 13 {:d} iteration x,y,z = 5, 5, 5: ".format(i),ans_array_13_1[i])
#for i in iter_range:
#    print("output 7 {:d} iteration x,y,z = 7, 7, 7 : ".format(i),ans_array_7_2[i])
#for i in iter_range:
#     print("output 13 {:d} iteration x,y,z = 7, 7, 7: ".format(i),ans_array_13_2[i])

difference_3 = np.empty(number_of_iter)
difference_5 = np.empty(number_of_iter)
difference_5_1 = np.empty(number_of_iter)
difference_3_1 = np.empty(number_of_iter)
difference_3_3 = np.empty(number_of_iter)
difference_5_3 = np.empty(number_of_iter)


for i in range(number_of_iter):
    difference_3[i] = ((abs(ans_array_7_2[i] -108))/108)*100
    difference_5[i] = ((abs(ans_array_13_2[i] -108))/108)*100
    difference_3_1[i] = ((abs(ans_array_7_1[i] -12))/12)*100
    difference_5_1[i] = ((abs(ans_array_13_1[i] -12))/12)*100
    difference_3_3[i] = ((abs(ans_array_7_3[i] -27))/27)*100
    difference_5_3[i] = ((abs(ans_array_13_3[i] -27))/27)*100
    #print(difference_3_3[i], difference_5_3[i] )
a_range = np.arange(0.,number_of_iter,1.)

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.plot(a_range,difference_3,'r--',label = 'D3Q7')
ax1.plot(a_range,difference_5,'g^',label = 'D3Q13')


plt.ylabel('percent difference')
plt.xlabel('iteration')
plt.title('Poisson Equation')
plt.legend()

ax2 = fig.add_subplot(312)
ax2.plot(a_range,difference_3_1,'r--',label = 'D3Q7')
ax2.plot(a_range,difference_5_1,'g^',label = 'D3Q13')
plt.ylabel('percent difference')
plt.xlabel('iteration')
plt.legend()

ax3 = fig.add_subplot(313)
ax3.plot(a_range,difference_3_3,'r--',label = 'D3Q7')
ax3.plot(a_range,difference_5_3,'g^',label = 'D3Q13')
plt.ylabel('percent difference')
plt.xlabel('iteration')
plt.legend()
plt.show()


#true_val_1 = np.empty(200)
#true_val_1.fill(75)
#true_val_2 = np.empty(200)
#true_val_2.fill(147)
#  
#fig = plt.figure()
#  
#ax1 = fig.add_subplot(311)
#ax1.plot(a_range,ans_array_7_1,'r--',label='D3Q7')
#ax1.plot(a_range,ans_array_13_1,'g^',label='D3Q13')
#ax1.plot(a_range,true_val_1,label='True Solution')
#plt.ylabel('value')
#plt.xlabel('iteration')
#plt.title('Poisson Equation')
#plt.legend()
#  
#ax2 = fig.add_subplot(312)
#ax2.plot(a_range,ans_array_7_2,'r--',label='D3Q7')
#ax2.plot(a_range,ans_array_13_2,'g^',label='D3Q13')
#ax2.plot(a_range,true_val_2,label='True Solution')
#plt.ylabel('value')
#plt.xlabel('iteration')
#plt.title('Poisson Equation')
#plt.legend()
#  
#  
#ax3 = fig.add_subplot(313)
#ax3.plot(a_range,difference,label='Diff. Between 7 and 13')
#plt.ylabel('difference')
#plt.xlabel('iteration')
#plt.legend()
#plt.show()

