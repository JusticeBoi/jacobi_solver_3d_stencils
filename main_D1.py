'''
Created on Sep 7, 2018

@author: oguz
'''
import numpy as np
import kernel as ker

def sett(ar,i,val):
    ar[i]=val
    return ar
    

A = np.array([[2,-1,0,0,0,0,0,0],
              [-1,2,-1,0,0,0,0,0],
              [0,-1,2,-1,0,0,0,0],
              [0,0,-1,2,-1,0,0,0],
              [0,0,0,-1,2,-1,0,0],
              [0,0,0,0,-1,2,-1,0],
              [0,0,0,0,0,-1,2,-1],
              [0,0,0,0,0,0,-1,2]])
input_array=np.array([0,0,0,0,0,0,0,0,0,81])
output_array = np.array([0,0,0,0,0,0,0,0,0,1])
rhs_array = np.array([2,2,2,2,2,2,2,2,2,2])
b = np.array([-2,-2,-2,-2,-2,-2,-2,78])

out=ker.ExecuteOneJacobiStepD1Q3(input_array, rhs_array, 2.0/3.0)
out=ker.ExecuteOneJacobiStepD1Q3(out, rhs_array, 2.0/3.0)

for i in range(300):
    out=ker.ExecuteOneJacobiStepD1Q3(out, rhs_array, 2.0/3.0)

print(out)

print(np.linalg.solve(A,b))
