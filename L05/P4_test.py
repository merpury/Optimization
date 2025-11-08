import numpy as np
from scipy.optimize import minimize

def z(f, r, R):
    return (1/np.sqrt(f)+2*np.log10((r/3.7)+(2.51/(R*np.sqrt(f)))))**2

def solve_colebrook(r, R):
    result = minimize(z, x0=0.02, args=(r, R), bounds=[(1e-6, 1)])
    return result.x[0]

if __name__ == '__main__':
    r = 0.0001476
    R = 132080.0
    fo = solve_colebrook(r, R)
    print(f'f = {fo} ; z(f) = {z(fo, r, R)}')