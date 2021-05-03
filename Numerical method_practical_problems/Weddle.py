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
def func(x):
    return 1/(1+(x**2))
def main():
    a = 0 #lower limit
    b = 1 #upper limit
    n = 2 #No. of steps
    s = 6
    h = ((b-a)/n)/s #interval
    i = a
    res = 0
    while True:
        f0 = func(i)
        f1 = func(i + h)
        f2 = func(i+(2*h))
        f3 = func(i+(3*h))
        f4 = func(i+(4*h))
        f5 = func(i+(5*h))
        f6 = func(i+(6*h))
        res = res + (((3*h)/10)*(f0 + (5*f1) + f2 + (6*f3) + f4 + (5*f5) + f6))
        i = i+(h*s)
        if i == b:
            break

    print("Integration value: ",res)
if __name__ == '__main__':
    main()