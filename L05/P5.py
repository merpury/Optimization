from scipy.optimize import minimize
import numpy as np

def Loss(location, base, distance):
    diff = location - base
    d1 = np.sum(diff ** 2, axis=1)
    return np.sum((d1 - distance.flatten() ** 2) ** 2)

def argmin_loss(base, distance):
    
    result = minimize(Loss, x0=np.array([3,4]), args=(base, distance))
    return result.x
    