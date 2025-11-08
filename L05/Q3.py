import numpy as np

# ==========================================================
# Q3: FONC CHECKS
# ==========================================================

def q3_1():
    # f(x) = (x-3.5)^2
    fprime = lambda x: 2*(x-3.5)
    cand = [3,3.5,4]
    P = [abs(fprime(x)) < 1e-9 for x in cand]
    # solution at 3.5 only
    sol = [x==3.5 for x in cand]
    return P, sol

def q3_2():
    # f(x)=4 sin(2πx)
    fprime = lambda x: 4*(2*np.pi)*np.cos(2*np.pi*x)
    cand = [0.25,0.3,0.75]
    P = [abs(fprime(x)) < 1e-9 for x in cand]
    # minima at π/2 → x=0.25 & 0.75 are local maxima/minima? check sign of second derivative
    # better check by evaluating f
    values = [4*np.sin(2*np.pi*x) for x in cand]
    # minimum among candidates
    min_val = min(values)
    sol = [values[i] == min_val for i in range(3)]
    return P, sol

def q3_3():
    # f(x)=25 + 0.2(x-5.2)^2
    fprime = lambda x: 0.4*(x-5.2)
    cand = [-1,5.2,5.4]
    P = [abs(fprime(x)) < 1e-9 for x in cand]
    # minimum clearly at 5.2
    sol = [x==5.2 for x in cand]
    return P, sol

def q3_4():
    # f(x1,x2)=(x1-4)^2 + (x2-3)^2
    def grad(x):
        x1,x2=x
        return np.array([2*(x1-4), 2*(x2-3)])
    cand = [np.array([4,0]), np.array([-4,3]), np.array([4,3])]
    P = [np.linalg.norm(grad(x)) < 1e-9 for x in cand]
    # minimum at (4,3)
    sol = [np.array_equal(x,np.array([4,3])) for x in cand]
    return P, sol

if __name__ == "__main__":
    print("\n======== Q3 ========")
    print("Q3.1:", q3_1())
    print("Q3.2:", q3_2())
    print("Q3.3:", q3_3())
    print("Q3.4:", q3_4())