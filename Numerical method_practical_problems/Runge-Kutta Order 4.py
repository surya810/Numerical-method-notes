#Runge-Kutta Method (Order 4)

"""
Name - Suryabrata Das

Sem: V    

College_Roll_NO: 703

Paper-code: CMSA DSE-IB

Registration No: A01-1112-117-003-2018

Examination roll_no: 2021151264

Subject: Numerical Methods (DSE-I)

"""
def func(x,y):
    return (x**2) + (y**2)
def main():
    x0 = 0
    y0 = 0
    xn = 0.4
    h = 0.1
    xi = x0
    yi = y0
    yn = 0
    while True:
        m1 = func(xi,yi)
        m2 = func((xi + (h/2)),(yi + ((h*m1)/2)))
        m3 = func((xi + (h/2)),(yi + ((h*m2)/2)))
        m4 = func((xi + h),(yi + (m1*h)))
        yn = yi +((h/6)*(m1 + (2*m2) + (2*m3) + m4))
        xi = xi + h
        yi = yn
        if xi == xn:
            break
    print("\ny(",xn,"): ", yn)
if __name__ == '__main__':
    main()