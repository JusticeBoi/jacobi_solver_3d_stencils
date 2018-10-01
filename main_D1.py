'''
Created on Sep 7, 2018

@author: oguz
'''
import numpy as np
import kernel as ker

A = np.array([[2,-1,0,0,0,0,0,0],
              [-1,2,-1,0,0,0,0,0],
              [0,-1,2,-1,0,0,0,0],
              [0,0,-1,2,-1,0,0,0],
              [0,0,0,-1,2,-1,0,0],
              [0,0,0,0,-1,2,-1,0],
              [0,0,0,0,0,-1,2,-1],
              [0,0,0,0,0,0,-1,2]])

##O(h²)
input_array_3=np.array([4.,0.,0.,0.,0.,0.,0.,0.,0.,121.])
output_array_3=np.copy(input_array_3)
# output_array = np.array([0,0,0,0,0,0,0,0,0,1])
rhs_array_3 = np.array([2,2,2,2,2,2,2,2,2,2])
b = np.array([-2,-2,-2,-2,-2,-2,-2,78])

##O(h⁴)
input_array_5=np.array([1.,4.,0.,0.,0.,0.,0.,0.,0.,0.,121.,144.])
output_array_5=np.copy(input_array_5)
rhs_array_5 = np.array([2,2,2,2,2,2,2,2,2,2,2,2])


# output_array_3=ker.ExecuteOneJacobiStepD1Q3(input_array_3,output_array_3, rhs_array_3, 2.0/3.0)
# out=ker.ExecuteOneJacobiStepD1Q3(out, rhs_array, 2.0/3.0)


output_array_5=ker.ExecuteOneJacobiStepD1Q5(output_array_5,output_array_5, rhs_array_5, 2.0/3.0)
# print(output_array_5)

relax = 2/3
for i in range(100):
    output_array_3=ker.ExecuteOneJacobiStepD1Q3(output_array_3,output_array_3, rhs_array_3, relax)
    output_array_5=ker.ExecuteOneJacobiStepD1Q5(output_array_5,output_array_5, rhs_array_5, relax)
      

# print(output_array_3)
print("d1q3: ",[x for x in output_array_3[1:-1]])
print("d1q5: ",[x for x in output_array_5[2:-2]])
# print(np.linalg.solve(A,b))
