#Bisection Methods

"""
Name - Suryabrata Das

Sem: V    

College_Roll_NO: 703

Paper-code: CMSA DSE-IB

Registration No: A01-1112-117-003-2018

Examination roll_no: 2021151264

Subject: Numerical Methods (DSE-I)

"""

def main():
    eq = "(x^2)-3"
    print ("Your Algebric/Transcendental Equation is: ",eq,"\n")
    a = 1
    b = 2
    e = 10**(-1*4) #precision
    bisection(a,b,e)
def bisection(a,b,e):
    if func(a)*func(b) >= 0:
        print("Your assumption is wrong about a and b!!")
        return
    c = float(a)
    iteration = 0
    while ((b-a) >= e):
        c = (a+b)/2
        if func(c) == 0.0:
            break
        if (func(c)*func(a) < 0):
                b = c
        elif (func(c)*func(b) < 0):
                a = c
        iteration += 1
        print("The root of the equation: ",c)
        print("Total iteration taken: ",iteration)
        
def func(x):

    return (x**2) - 3
if __name__ == '__main__':
    main()