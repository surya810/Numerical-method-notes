#Newton Raphson Methods

"""
Name - Suryabrata Das

Sem: V    

College_Roll_NO: 703

Paper-code: CMSA DSE-IB

Registration No: A01-1112-117-003-2018

Examination roll_no: 2021151264

Subject: Numerical Methods (DSE-I)

"""
from sympy import *

def newton_raphson(f,f_prime,a,e):
    h = f(a)/f_prime(a)
    while abs(h) >= e:
        h = f(a)/f_prime(a)
        a = a - h
    print("The root of the equation is: ",a)
def main():
    x = Symbol('x')
    f = x**3 - x - 3
    f_prime = f.diff(x)
    print("Your function: ",f);
    print("Derivative of the function: ",f_prime)
    f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    a = 1
    e = 10**(-1*5)
    newton_raphson(f,f_prime,a,e)
if __name__ == '__main__':
    main()