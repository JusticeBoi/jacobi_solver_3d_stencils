'''
Created on Sep 7, 2018

@author: oguz
'''
grid_size = 8
delta_x = 1
import numpy as np
#define COMP_CELL_IDX(I,J,K,N) ((I)*(N[Y]+2)*(N[Z]+2) + (J)*(N[Z]+2) + (K))

def getDataGhostQ7(a_np_array,i,j,k):
    ''' if input 0 0 0 is ghost '''
    return a_np_array[(i*100)+(j*10)+k]

def getDataQ7(a_np_array,i,j,k):
    '''Gets non-ghost data, if input is 0 0 0, gets 1 1 1 which is not ghost '''
    
    return a_np_array[((i+1)*100)+((j+1)*10)+k+1]

def setDataGhostQ7(a_np_array,i,j,k,val):
    a_np_array[(i*100)+(j*10)+k] = val
    return a_np_array

def setDataQ7(a_np_array,i,j,k,val):
    a_np_array[((i+1)*100)+((j+1)*10)+k+1] = val
    return a_np_array

#TODO: now write the D313 version and compare convergence behaviour     
def ExecuteOneJacobiStepD3Q7(input_array,rhs_array,relax_param):
    for i in range(8):
        for j in range(8):
            for k in range(8):
                v= 0
                fct = 0
                
                v+=(getDataQ7(input_array, i+1, j, k)*(1/pow(delta_x,2)))
                fct+=(1/pow(delta_x,2))
                
                v+=(getDataQ7(input_array, i-1, j, k)*(1/pow(delta_x,2)))
                fct+=(1/pow(delta_x,2))
                
                v+=(getDataQ7(input_array, i, j+1, k)*(1/pow(delta_x,2)))
                fct+=(1/pow(delta_x,2))
                
                v+=(getDataQ7(input_array, i, j-1, k)*(1/pow(delta_x,2)))
                fct+=(1/pow(delta_x,2))
                
                v+=(getDataQ7(input_array, i, j, k+1)*(1/pow(delta_x,2)))
                fct+=(1/pow(delta_x,2))
                
                v+=(getDataQ7(input_array, i, j, k-1)*(1/pow(delta_x,2)))
                fct+=(1/pow(delta_x,2))
                
                val = relax_param*((v-getDataQ7(rhs_array,i,j,k))/fct) + (1-relax_param) *getDataQ7(input_array,i,j,k)
                
                input_array = setDataQ7(input_array, i, j, k, val)
    
    return input_array
                

def setD1Q3(output_array,i,val):
    output_array[i] = val
    return output_array
 
def ExecuteOneJacobiStepD1Q3(input_array,rhs_array,relax_param):
    out_array = np.zeros(len(input_array))
    out_array[0] = input_array[0]
    out_array[9] = input_array[9]
    for i in range(8):
        v= 0
        fct = 0
        v += input_array[i+2]*(1/pow(delta_x,2))
        fct+=(1/pow(delta_x,2))
        v += input_array[i]*(1/pow(delta_x,2))
        fct+=(1/pow(delta_x,2))
        val = relax_param * ((v-rhs_array[i+1])/fct) + (1-relax_param)*input_array[i+1]
        out_array=setD1Q3(out_array,i+1,val)
    return out_array 
        
        
