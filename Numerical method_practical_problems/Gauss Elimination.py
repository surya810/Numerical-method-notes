#Basic Gauss Elimination Methods


"""
Name - Suryabrata Das

Sem: V    

College_Roll_NO: 703

Paper-code: CMSA DSE-IB

Registration No: A01-1112-117-003-2018

Examination roll_no: 2021151264

Subject: Numerical Methods (DSE-I)

"""
import numpy as np
def swap_row(mat,r1,r2):
    temp = mat[r1]
    mat[r1] = mat[r2]
    mat[r2] = temp
    
    
def normalize(mat,i):
    for j in range(i+1,len(mat)):
        fact = (mat[j][i]/mat[i][i])
        for k in range(0,len(mat)+1):
            mat[j][k] -= fact*mat[i][k]

def fwd_elimination(mat):
    n = len(mat)
    print("\n\n")
    for i in range(n-1):
        if mat[i][i] == 0:
            swap_row(mat,i,i+1)
            normalize(mat,i)
            m = np.array(mat)
            m = m[:,:n]
            if (np.linalg.det(m) == 0):
                print ("Singular Matrix!! No Unique solution Exists!!")
                return False
            
            return True

def print_mat(mat):
    for i in range(len(mat)):
        print(mat[i])
        print("\n")
def bwd_elimination(mat):
    n = len(mat)

    x = [0]*n
    for i in range(n-1,-1,-1):
        x[i] = mat[i][n]
        for j in range(i+1,n):
            x[i] -= mat[i][j]*x[j]
            x[i] = x[i]/mat[i][i]
            print("Solutions are: \n\n")
            print("x: ",x[0],"\n\n")
    print("y: ",x[1],"\n\n")
    print("z: ",x[2],"\n\n")

def main():
    n = 3
    mat = []
    mat = [[3,6,1,16],[2,4,3,13],[1,3,2,9]]
    print("Your input matrix: ")
    print_mat(mat)
    if(fwd_elimination(mat) == True):
        print("After Forward Elimination: ")
        print_mat(mat)
        bwd_elimination(mat)
if __name__ == '__main__':
    main()