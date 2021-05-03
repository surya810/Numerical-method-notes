#Regula Falsy Methods

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
    eq = "3x^2 + 6x - 45"
    print ("Your Algebric/Transcendental Equation is: ",eq)
    a = 2.5
    b = 3.5
    e = 10**(-1*4)
    regula_falsy(a,b,e)
def regula_falsy(a,b,e):
    if func(a)*func(b) >= 0:
        print("Your assumption is wrong about a and b!!")
        return
    c = float(a)
    iteration = 1
    while ((b-a) >= e):
        c = b - ((func(b)*(b-a))/(func(b)-func(a)))
        if func(c) == 0.0:
            break
        if (func(c)*func(a) < 0):
            b = c
        elif (func(c)*func(a) > 0):
                a = c
                iteration += 1
                print("The root of the equation: ",c)
                print("Total iteration taken: ",iteration)

def func(x):

    return (3*(x**2)) + (6*x) - 45
if __name__ == '__main__':
    main()