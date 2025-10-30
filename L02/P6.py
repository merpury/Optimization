"""
Write a function implementing Bisection.
"""

# from matplotlib import pyplot as plt
# import numpy as np
def fpolynomial(root, root_const):
    # y = root_const[0]*root**2 + root_const[1]*root + root_const[2]
    y = root_const[0] + root_const[1]*root + root_const[2]*root**2
    return y

def fq(x):
    y = -5 + x + x**2
    return y

def bisection(a, b, TOL):

    fa = fq(a)
    #fb = fq(b)

    while abs(a - b) > TOL:
        c = (a + b) / 2

        fc = fq(c)

        if fc == 0:
            return c

        else:

            if fc * fa > 0:
                # Complete the code here
                a = c
            else:
                b = c

    return (a + b)/2

## Don't edit below this line.
## ====================================================

if __name__ == '__main__':

    xa = float(input('a:'))
    xb = float(input('b:'))
    tol = float(input('TOL:'))

    root = bisection(xa, xb, tol)
    print("f({:,.3f})={:,.5f}".format(root, fpolynomial(root, [-5, 1, 1])))

