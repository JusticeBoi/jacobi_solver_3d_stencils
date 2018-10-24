'''
Created on Sep 7, 2018
@author: oguz
PROBLEM IS PRESSURE POISSON EQUATION IF P IS GIVEN AS P(X) = X² or P(X) = x³
'''
import numpy as np
import matplotlib.pyplot as plt
import kernel as ker
from math import exp
number_of_iter = 10000
delta_x = 0.015625

input_array_3_64 = np.zeros(65)

input_array_5_64 = np.zeros(65)
input_array_5_64[1] = -5.08627295e-03

input_array_5_64[63] = -1.19537115e-04


rhs_array_3_16 = np.zeros(65)

dif_3 = np.zeros(65)
dif_5 = np.zeros(65)

for i in range(65):
    rhs_array_3_16[i] = 1 - 2 * (delta_x * i) * (delta_x * i)


output_array_3_64 = np.copy(input_array_3_64)
output_array_5_64 = np.copy(input_array_5_64)



relax = 2.0/3.0


ans_array_3_1 = np.zeros(number_of_iter)
ans_array_5_1 = np.zeros(number_of_iter)
percent_error_3_through_iterations = np.zeros(number_of_iter)
percent_error_5_through_iterations = np.zeros(number_of_iter)

real_sol = np.zeros(65)
for i in range(65):
    real_sol[i] = ((i*delta_x*delta_x*i)/2) - ((pow(i*delta_x,4)) / 6 ) - (i*delta_x / 3 )

for i in range(number_of_iter):
    input_array_3_64 = ker.ExecuteOneJacobiStepD1Q3(input_array_3_64,output_array_3_64, rhs_array_3_16, relax)
    input_array_5_64 = ker.ExecuteOneJacobiStepD1Q5(input_array_5_64,output_array_5_64, rhs_array_3_16, relax)
    ans_array_3_1[i] = ker.getDataQ3(output_array_3_64,3)
    ans_array_5_1[i] = ker.getDataGhostQ5(output_array_5_64,3)
    #if(i == 5000):
    #    print("output_array_3_64: ",output_array_3_64)
    #    print("output_array_5_64: ",output_array_5_64)
    for j in range(1,64):
        dif_3[j] = ((abs(output_array_3_64[j] - real_sol[j]))/abs(real_sol[j])) * 100
        dif_5[j] = ((abs(output_array_5_64[j] - real_sol[j]))/abs(real_sol[j])) * 100
    #if(i == 5000):
    #    print("diff3: ",dif_3)
    #    print("diff5: ",dif_5)
    percent_error_3 = 0
    percent_error_5 = 0
    for j in range(1,64):
        percent_error_3 += dif_3[j]
        percent_error_5 += dif_5[j]
    percent_error_3 /= 63
    percent_error_5 /= 61
    if(i == 9000 or i == 9500):
        print("percent_error_3 : ",percent_error_3)
        print("percent_error_5 : ",percent_error_5)
    percent_error_3_through_iterations[i] = percent_error_3
    percent_error_5_through_iterations[i] = percent_error_5



print("d1q3 : ",output_array_3_64 )
print("d1q5 : ",output_array_5_64 )
print("real sol : ",real_sol )





difference_3 = np.empty(100)

difference_5 = np.empty(100)





for i in range(100):
    difference_3[i] = ((abs(ans_array_3_1[i] - real_sol[3]))/abs(real_sol[3]))*100
    difference_5[i] = ((abs(ans_array_5_1[i] - real_sol[3]))/abs(real_sol[3]))*100

#fig = plt.figure()
#ax1 = fig.add_subplot(311)
#ax1.plot(a_range,difference_3,'r--',label='D1Q3')
#ax1.plot(a_range,difference_5,'g^',label='D1Q5')
#ax1.set_xscale('log')
#plt.ylabel('percent difference from real value ')
#plt.xlabel('number of iteration')
#plt.title('Poisson Equation')
#plt.legend()

a_range = np.arange(0.,number_of_iter)
plt.plot(a_range,percent_error_3_through_iterations,'-r',label='D1Q3')
plt.plot(a_range,percent_error_5_through_iterations,'-g',label='D1Q5')
plt.ylabel('average percent difference')
plt.xlabel('iteration')
#plt.semilogx()
plt.legend()
plt.show()

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
