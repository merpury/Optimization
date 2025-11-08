import numpy as np
from scipy.optimize import minimize

def Loss(Location, Bases, Distances):
    diff = Location - Bases
    d1 = np.sum(diff**2, axis=1)
    return np.sum((d1 - Distances.flatten() **2)**2)

def argmin_loss(Bases, Distances):
    result = minimize(Loss, x0=np.array([3,4]), args=(Bases, Distances))
    return result.x

if __name__ == '__main__':
    BRef = np.array([[100, 0], [100, 100], [0, 100],
    [0, 0], [-20, 50]])
    # The ground-truth position of the device
    gt = np.array((30, 70)).reshape((1,2))
    # The distance
    D = np.sqrt(np.sum( (BRef - gt)**2, axis = 1 )).reshape(-1,1)
    P = np.array([30, 70])
    print(Loss(P, BRef, D))
    P = np.array([31, 71])
    print(Loss(P, BRef, D))
    P = np.array([29, 70])
    print(Loss(P, BRef, D))
    print(f"Location = {argmin_loss(BRef, D)}")
    # Test 2
    gt = np.array((15, 40)).reshape((1,2))
    D = np.sqrt(np.sum( (BRef - gt)**2, axis = 1 )).reshape(-1,1)
    print(f"Location = {argmin_loss(BRef, D)}")