'''
Created on Sep 7, 2018
@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X) = X² or P(X) = x³
'''
import numpy as np
import matplotlib.pyplot as plt
import kernel as ker
from math import exp

delta_x = 0.0625

input_array_3_16 = np.zeros(17)

input_array_5_16 = np.zeros(17)
input_array_5_16[1] = -1.88827515e-02

input_array_5_16[15] =-1.79290771e-03


rhs_array_3_16 = np.zeros(17)

for i in range(17):
    rhs_array_3_16[i] = 1 - 2 * (0.0625 * i) * (0.0625 * i)


output_array_3_16 = np.copy(input_array_3_16)
output_array_5_16 = np.copy(input_array_5_16)



relax = 2.0/3.0


ans_array_3_1 = np.zeros(100)
ans_array_5_1 = np.zeros(100)

for i in range(100):
    input_array_3_16 = ker.ExecuteOneJacobiStepD1Q3(input_array_3_16,output_array_3_16, rhs_array_3_16, relax)
    input_array_5_16 = ker.ExecuteOneJacobiStepD1Q5(input_array_5_16,output_array_5_16, rhs_array_3_16, relax)
    ans_array_3_1[i] = ker.getDataQ3(output_array_3_16,3)
    ans_array_5_1[i] = ker.getDataGhostQ5(output_array_5_16,3)
real_sol = np.zeros(17)

for i in range(17):
    real_sol[i] = ((i*0.0625*0.0625*i)/2) - ((pow(i*0.0625,4)) / 6 ) - (i*0.0625 / 3 )

print("d1q3 : ",output_array_3_16 )
print("d1q5 : ",output_array_5_16 )
print("real sol : ",real_sol[3] )





difference_3 = np.empty(100)

difference_5 = np.empty(100)





for i in range(100):
    difference_3[i] = ((abs(ans_array_3_1[i] - real_sol[3]))/abs(real_sol[3]))*100
    difference_5[i] = ((abs(ans_array_5_1[i] - real_sol[3]))/abs(real_sol[3]))*100
a_range = np.arange(0.,100.,1.)
print(ans_array_5_1)
print(real_sol[3])

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax1.plot(a_range,difference_3,'r--',label='D1Q3')
ax1.plot(a_range,difference_5,'g^',label='D1Q5')
ax1.set_xscale('log')
plt.ylabel('percent difference from real value ')
plt.xlabel('number of iteration')
plt.title('Poisson Equation')
plt.legend()


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
plt.show()
#
