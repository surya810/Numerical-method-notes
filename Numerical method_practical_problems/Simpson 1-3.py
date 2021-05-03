#Simpson's 1/3 Rule

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
def func(x):
    return np.exp((-x/2))
def main():
    a = 1 #lower limit
    b = 2 #upper limit
    n = 4 #No. of steps
    s = 2
    h = ((b-a)/n)/s #interval
    i = a
    res = 0
    while True:
        res = res +((h*(func(i) + (4*func(i+h)) + func(i+(2*h))))/3)
        i = i+(h*s)
        if i == b:
            break
    print("Integration value: ",res)
if __name__ == '__main__':
    main()
