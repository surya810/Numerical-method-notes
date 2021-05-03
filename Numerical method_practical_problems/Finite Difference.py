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
	
def bwd_elimination(mat):
	n = len(mat)
	x = [0]*n
	
	for i in range(n-1,-1,-1):
		x[i] = mat[i][n]
		
		for j in range(i+1,n):
			x[i] -= mat[i][j]*x[j]
			
		x[i] = x[i]/mat[i][i]
		
	print("Solutions are: \n\n")
	print("y(0.25): ",x[0],"\n\n")
	print("y(0.5): ",x[1],"\n\n")
	print("y(0.75): ",x[2],"\n\n")

def func(x):
	return np.exp(x**2)
		 
def main(): 
	mat = []
	y0 = 0; y4 = 0;
	h = 0.25;
	x = [0.25,0.5,0.75]
	f = []
	for i in range(3):
		temp = func(x[i])*(h**2)
		f.append(temp)
		
	f[0] -= y0;
	f[2] -= y4;
	  	
	mat = [[-2,1,0,f[0]],[1,-2,1,f[1]],[0,1,-2,f[2]]]
	
	if(fwd_elimination(mat) == True):
		bwd_elimination(mat)
	
if __name__ == '__main__':
	main()
	

