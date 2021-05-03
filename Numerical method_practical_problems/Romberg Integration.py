#Romberg Integration

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
import matplotlib.pyplot as plt
def f1(x):
    f1 = np.sin(x)
    return f1;

# trapezoidal rule
def trapezoid(f,a,b,N):
    h = (b-a)/N
    xi = np.linspace(a,b,N+1)
    fi = f(xi)
    s = 0.0
    for i in range(1,N):
        s = s + fi[i]
    s = (h/2)*(fi[0] + fi[N]) + h*s
    return s

# romberg method starts from here

def romberg(f,a,b,eps,nmax):
# f ... function to be integrated
# [a,b] ... integration interval
# eps ... desired accuracy
# nmax ... maximal order of Romberg method
    Q = np.zeros((nmax,nmax),float)
    converged = 0
    for i in range(0,nmax):
        N = 2**i
        Q[i,0] = trapezoid(f,a,b,N)
        for k in range(0,i):
            n = k + 2
            Q[i,k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*Q[i,k] - Q[i-1,k])
        if (i > 0):
            if (abs(Q[i,k+1] - Q[i,k]) < eps):
                converged = 1

                break
            print("Integral Value: ",Q[i,k+1])
# main program
a = 0.0;b = 1.0 # integration interval [a,b]
romberg(f1,a,b,1.0e-12,10)



