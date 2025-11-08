import numpy as np
from scipy.optimize import minimize, fsolve

def z(f, r, R):
    return 1.0/np.sqrt(f) + 2.0*np.log10( (r/3.7) + 2.51/(R*np.sqrt(f)) )

def colebrook_sq(f, r, R):
    return z(f, r, R)**2 

def solve_colebrook(r, R):
    
    result = minimize(colebrook_sq, x0=0.02, args=(r,R), bounds=[(1e-6, 1.0)])
    return result.x[0]

if __name__ == '__main__':
    r = 0.0001476
    R = 132080.0
    fo = solve_colebrook(r, R)
    print(f'f = {fo} ; z(f) = {z(fo, r, R)}')