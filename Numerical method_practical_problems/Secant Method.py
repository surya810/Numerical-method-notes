#Secant Method

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
def main():
    eq = "4x^3 - 2x - 6"
    x = Symbol('x')
    f = (4 * x**3) - (2*x) - 6
    f = lambdify(x, f)
    print ("Your Algebric/Transcendental Equation is: ",eq)
    a = 1
    b = 2
    e = 8
    secant(f,a,b,e)
def secant(f,a,b,e):
    c = float(a)
    iteration = 0
    while (iteration <= e):
        c = b - ((f(b)*(b-a))/(f(b)-f(a)))
        a = b
        b = c
        iteration += 1
    print("The root of the equation (appx.): ",c)
if __name__ == '__main__':
    main()
