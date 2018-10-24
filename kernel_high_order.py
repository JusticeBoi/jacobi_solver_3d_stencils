'''
Created on Sep 7, 2018

@author: oguz
'''
grid_size = 8
delta_x = 1
delta_x_9 = 1.0
delta_x_9_sqr = 1/pow(delta_x_9,2)
delta_x_7 = 1.0
delta_x_13 = 1.0
five_over_12 = 5.0/12.0

import numpy as np
#define COMP_CELL_IDX(I,J,K,N) ((I)*(N[Y]+2)*(N[Z]+2) + (J)*(N[Z]+2) + (K))

##D1Q3 functions
def getDataD1NonUni(a_np_array,i):
    return a_np_array[i+1]

def setDataD1NonUni(a_np_array,i,val):
    a_np_array[i+1] = val
    return a_np_array

def ExecuteOneJacobiStepD1NonUnii(input_array,output_array,rhs_array,relax_param):
    print("asd")
    for i in range(10):
        v = 0
        fct = 0
        if i == 0 or i == 9:
            print("asd")
            v += getDataD1NonUni(input_array,i+1)*(1/pow(delta_x,2))
            fct += (1/pow(delta_x,2))
            v += getDataD1NonUni(input_array,i-1)*(1/pow(delta_x,2))
            fct += (1/pow(delta_x,2))

            val = relax_param * ((v-getDataD1NonUni(rhs_array,i))/fct) + (1-relax_param)*getDataD1NonUni(input_array,i)
            setDataD1NonUni(output_array,i,val)
        else:
            print("asd")
            v += (-1*getDataD1NonUni(input_array,i+2)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            v += ((16.)*getDataD1NonUni(input_array,i+1)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            v += (-1*getDataD1NonUni(input_array,i-2)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            v += ((16.)*getDataD1NonUni(input_array,i-1)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            val = relax_param * ((v-getDataD1NonUni(rhs_array,i))/fct) + (1-relax_param)*getDataD1NonUni(input_array,i)
            setDataD1NonUni(output_array,i,val)
    return output_array

def setD1Q3(output_array,i,val):
    output_array[i] = val
    return output_array



def setDataQ3(a_np_array,i,val):
    a_np_array[i+1] = val
    return a_np_array

def getDataQ3(a_np_array,i):
    return a_np_array[i]

def ExecuteOneJacobiStepD1Q3(input_array,output_array,rhs_array,relax_param):
    for i in range(10):
        v= 0
        fct = 0
        v += input_array[i+2]*(1/pow(delta_x,2))
        fct+=(1/pow(delta_x,2))
        v += input_array[i]*(1/pow(delta_x,2))
        fct+=(1/pow(delta_x,2))
        val = relax_param * ((v-rhs_array[i+1])/fct) + (1-relax_param)*input_array[i+1]
        #output_array[i+1] = val
        setDataQ3(output_array,i,val) 
    return output_array

def ExecuteOneJacobiStepD1Q3Large(input_array,output_array,rhs_array,relax_param):
    for i in range(98):
        v= 0
        fct = 0
        
        v += input_array[i+2]*(1/pow(delta_x,2))
        fct+=(1/pow(delta_x,2))
        v += input_array[i]*(1/pow(delta_x,2))
        fct+=(1/pow(delta_x,2))
        
        val = relax_param * ((v-rhs_array[i+1])/fct) + (1-relax_param)*input_array[i+1]
        output_array[i+1] = val
    return output_array 

##D1Q5 functions
def getDataGhostQ5(a_np_array,i):
    ''' if input 0 0 0 is ghost '''
    return a_np_array[i]

def getDataQ5(a_np_array,i):
    '''Gets non-ghost data, if input is 0 0 0, gets 1 1 1 which is not ghost '''
    return a_np_array[i+2]

def setDataQ5(a_np_array,i,val):
    a_np_array[i+2] = val
    return a_np_array
def getDataD1NonUni(a_np_array,i):
    return a_np_array[i+1]

def setDataD1NonUni(a_np_array,i,val):
    a_np_array[i+1] = val
    return a_np_array

def ExecuteOneJacobiStepD1NonUni(input_array,output_array,rhs_array,relax_param):
    for i in range(8):
        v = 0
        fct = 0
        if i == 0 or i == 7:
            v += getDataD1NonUni(input_array,i+1)*(1/pow(delta_x,2))
            fct += (1/pow(delta_x,2))
            v += getDataD1NonUni(input_array,i-1)*(1/pow(delta_x,2))
            fct += (1/pow(delta_x,2))

            val = relax_param * ((v-getDataD1NonUni(rhs_array,i))/fct) + (1-relax_param)*getDataD1NonUni(input_array,i)
            setDataD1NonUni(output_array,i,val)
        else:
            v += (-1*getDataD1NonUni(input_array,i+2)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            v += ((16.)*getDataD1NonUni(input_array,i+1)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            v += (-1*getDataD1NonUni(input_array,i-2)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            v += ((16.)*getDataD1NonUni(input_array,i-1)*(1/pow(delta_x,2))* (1./12.))
            fct += ((1/pow(delta_x,2))*0.625)

            val = relax_param * ((v-getDataD1NonUni(rhs_array,i))/fct) + (1-relax_param)*getDataD1NonUni(input_array,i)
            setDataD1NonUni(output_array,i,val)
    return output_array

def ExecuteOneJacobiStepD1Q5(input_array,output_array,rhs_array,relax_param):
    for i in range(8):
        v= 0
        fct = 0
        
        v += (-1*getDataQ5(input_array,i+2)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        v += ((16.)*getDataQ5(input_array,i+1)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        
        v += (-1*getDataQ5(input_array,i-2)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        v += ((16.)*getDataQ5(input_array,i-1)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        
        val = relax_param * ((v-getDataQ5(rhs_array,i))/fct) + (1-relax_param)*getDataQ5(input_array,i)
        setDataQ5(output_array,i,val)
    return output_array 
            
def ExecuteOneJacobiStepD1Q5Large(input_array,output_array,rhs_array,relax_param):
    for i in range(98):
        v= 0
        fct = 0
        
        v += (-1*getDataQ5(input_array,i+2)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        v += ((16.)*getDataQ5(input_array,i+1)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        
        v += (-1*getDataQ5(input_array,i-2)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        v += ((16.)*getDataQ5(input_array,i-1)*(1/pow(delta_x,2))* (1./12.))
        fct+=((1/pow(delta_x,2))*0.625)
        
        val = relax_param * ((v-getDataQ5(rhs_array,i))/fct) + (1-relax_param)*getDataQ5(input_array,i)
        setDataQ5(output_array,i,val)
    return output_array 
##D2Q9 functions
def setDataGhostD2Q9(a_np_array,i,j,val):
    a_np_array[(i*10)+j] = val
    return a_np_array

def setDataD2Q9(a_np_array,i,j,val):
    a_np_array[((i+1)*10)+ j +1] = val
    return a_np_array

def getDataGhostD2Q9(a_np_array,i,j):
    ''' if input 0 0 0 is ghost '''
    return a_np_array[(i*10)+j]

def getDataD2Q9(a_np_array,i,j):
    '''Gets non-ghost data, if input is 0 0 0, gets 1 1 1 which is not ghost '''
    return a_np_array[((i+1)*10) + (j +1) ]

def ExecuteOneJacobiStepD2Q9(input_array,output_array,rhs_array,relax_param):
    for i in range(8):
        for j in range(8):
            v = 0
            fct = 0
            
            v+=(getDataD2Q9(input_array, i-1, j+1)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
                
            v+=(4.0*getDataD2Q9(input_array, i, j+1)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
            
            v+=(getDataD2Q9(input_array, i+1, j+1)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
            
            v+=(4.0*getDataD2Q9(input_array, i-1, j)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
            
            v+=(4.0*getDataD2Q9(input_array, i+1, j)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
            
            v+=(getDataD2Q9(input_array, i-1, j-1)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
            
            v+=(4.0*getDataD2Q9(input_array, i, j-1)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
            
            v+=(getDataD2Q9(input_array, i+1, j-1)*delta_x_9_sqr*(1.0/6.0))
            fct+=(delta_x_9_sqr*five_over_12)
            
            
            val = relax_param*((v-getDataD2Q9(rhs_array,i,j))/fct) + (1-relax_param) *getDataD2Q9(input_array,i,j)
            output_array = setDataD2Q9(output_array, i, j, val)
            
    return output_array
            
            
            
            
            
            
    
##D3Q7 functions        
        
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

def ExecuteOneJacobiStepD3Q7(input_array,output_array,rhs_array,relax_param):
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                v= 0
                fct = 0
                
                v+=(getDataQ7(input_array, i+1, j, k)*(1/pow(delta_x_7,2)))
                fct+=(1/pow(delta_x_7,2))
                
                v+=(getDataQ7(input_array, i-1, j, k)*(1/pow(delta_x_7,2)))
                fct+=(1/pow(delta_x_7,2))
                
                v+=(getDataQ7(input_array, i, j+1, k)*(1/pow(delta_x_7,2)))
                fct+=(1/pow(delta_x_7,2))
                
                v+=(getDataQ7(input_array, i, j-1, k)*(1/pow(delta_x_7,2)))
                fct+=(1/pow(delta_x_7,2))
                
                v+=(getDataQ7(input_array, i, j, k+1)*(1/pow(delta_x_7,2)))
                fct+=(1/pow(delta_x_7,2))
                
                v+=(getDataQ7(input_array, i, j, k-1)*(1/pow(delta_x_7,2)))
                fct+=(1/pow(delta_x_7,2))
                
                val = relax_param*((v-getDataQ7(rhs_array,i,j,k))/fct) + (1-relax_param) *getDataQ7(input_array,i,j,k)
                output_array = setDataQ7(output_array, i, j, k, val)
    
    return output_array
          


##D3Q13 functions
def getDataGhostQ13(a_np_array,i,j,k):
    ''' if input 0 0 0 is ghost '''
    return a_np_array[(i*100)+(j*10)+k]

def getDataQ13(a_np_array,i,j,k):
    '''Gets non-ghost data, if input is 0 0 0, gets 1 1 1 which is not ghost '''
    
    return a_np_array[((i+2)*100)+((j+2)*10)+k+2]

def setDataGhostQ13(a_np_array,i,j,k,val):
    a_np_array[(i*100)+(j*10)+k] = val
    return a_np_array

def setDataQ13(a_np_array,i,j,k,val):
    a_np_array[((i+2)*100)+((j+2)*10)+k+2] = val
    return a_np_array


def ExecuteOneJacobiStepD3Q13(input_array,output_array,rhs_array,relax_param):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                v= 0
                fct = 0
                
                v+=(-1*getDataQ13(input_array, i+2, j, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                v+=(16*getDataQ13(input_array, i+1, j, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                v+=(-1*getDataQ13(input_array, i-2, j, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                v+=(16*getDataQ13(input_array, i-1, j, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                
                v+=(-1*getDataQ13(input_array, i, j+2, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                v+=(16*getDataQ13(input_array, i, j+1, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                v+=(-1*getDataQ13(input_array, i, j-2, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                v+=(16*getDataQ13(input_array, i, j-1, k)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2))*0.625 )
                
                
                v+=(-1*getDataQ13(input_array, i, j, k+2)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2)) * 0.625 )
                
                v+=(16*getDataQ13(input_array, i, j, k+1)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2)) * 0.625 )
                
                v+=(-1*getDataQ13(input_array, i, j, k-2)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2)) * 0.625 )
                
                v+=(16*getDataQ13(input_array, i, j, k-1)*(1/pow(delta_x_13,2))*(1.0/12.0))
                fct+=((1/pow(delta_x_13,2)) * 0.625 )
                
                val = relax_param*((v-getDataQ13(rhs_array,i,j,k))/fct) + (1-relax_param) * getDataQ13(input_array,i,j,k)
                
                
                output_array = setDataQ13(output_array, i, j, k, val)
                
    return output_array
                
                


