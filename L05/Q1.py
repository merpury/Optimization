import numpy as np

# ==========================================================
# Q1 FUNCTIONS
# ==========================================================

def q1_1():
    # g(u) = 2u if u>=3 ; g(u)= (9-u)+1 if u<3
    def g(u):
        return 2*u if u >= 3 else (9-u)+1
    # Minimum occurs at checking derivative: but piecewise linear → check boundary at u=3
    # Left branch slope = -1 , right branch slope = 2 → minimum at boundary u = 3
    u = 3
    return u, g(u)

def q1_2():
    # g(u)=(u−17)^2 → minimum at u = 17
    g = lambda u: (u-17)**2
    u = 17
    return u, g(u)

def q1_3():
    g = lambda u: (u-19)**2 + 198
    u = 19
    return u, g(u)

def q1_4():
    g = lambda u: (u-18)**2 - 176
    u = 18
    return u, g(u)

def q1_5():
    # max g(u) = −(u + 15)^2 −124  → concave (negative square)
    # maximum at vertex u = -15
    g = lambda u: -(u+15)**2 - 124
    u = -15
    return u, g(u)

def q1_6():
    # max exp(-(u-4.5)^2) → peak at u = 4.5
    g = lambda u: np.exp(-(u-4.5)**2)
    u = 4.5
    return u, g(u)

def q1_7():
    # max 4u+2  s.t. u ≤ 12.5 → linear increasing → choose max feasible
    g = lambda u: 4*u + 2
    u = 12.5
    return u, g(u)

def q1_8():
    g = lambda u: 0.2*np.sin(120*u + np.pi)
    # Maximize inside interval → scan grid
    U = np.linspace(0, 0.06, 20000)
    vals = g(U)
    idx = np.argmax(vals)
    return U[idx], vals[idx]

def q1_9():
    g = lambda u: 0.2*np.sin(120*u + np.pi)
    U = np.linspace(0, 0.06, 20000)
    vals = g(U)
    idx = np.argmin(vals)
    return U[idx], vals[idx]

def q1_10():
    # discrete {0,1}
    def g(x):
        if x == -1: return -1
        if x == 0: return 1
        if x == 1: return 0
    # but feasible is {0,1}
    candidates = [0, 1]
    best = min(candidates, key=lambda x: g(x))
    return best, g(best)

def q1_11():
    # f(u1,u2) = (3−u1)^2 (2−2u2+u2^2)
    def f(u1,u2):
        return (3-u1)**2 * (2-2*u2+u2*u2)
    U = np.linspace(0,2,1001)
    best_val = 1e18
    best_u1 = None
    best_u2 = None
    for u1 in U:
        for u2 in U:
            val = f(u1,u2)
            if val < best_val:
                best_val = val
                best_u1 = u1
                best_u2 = u2
    return best_u1, best_u2, best_val

def q1_12():
    A = np.array([[1,0],[0,-1]])
    candidates = [np.array([0,0]),
                  np.array([0,1]),
                  np.array([1,0]),
                  np.array([1,1])]
    def f(u):
        return u.T @ A @ u
    best = min(candidates, key=lambda u: f(u))
    return best, f(best)

if __name__ == "__main__":
    print("======== Q1 ========")
    print("Q1.1:", q1_1())
    print("Q1.2:", q1_2())
    print("Q1.3:", q1_3())
    print("Q1.4:", q1_4())
    print("Q1.5:", q1_5())
    print("Q1.6:", q1_6())
    print("Q1.7:", q1_7())
    print("Q1.8:", q1_8())
    print("Q1.9:", q1_9())
    print("Q1.10:", q1_10())
    print("Q1.11:", q1_11())
    print("Q1.12:", q1_12())