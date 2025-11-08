import numpy as np
# ==========================================================
# Q2
# ==========================================================

def q2():
    ans = {}
    # Q2.1 : argmin(-f(x)) = maximizer of f(x)
    ans["Q2.1"] = -3.4

    # Q2.2 : argmin(10 - f(x)) = argmax(f(x))
    ans["Q2.2"] = 43.12

    # Q2.3 : argmin(10 + f(x))  → f(x) is irrelevant (monotonic) → no information
    ans["Q2.3"] = "?"

    # Q2.4 : min f(x) given argmax(0.78 - f(x)) = argmin(f(x))
    ans["Q2.4"] = 0.78

    # Q2.5 : argmin(0.78 - f(x)) → argmax(f(x)) ; but we want argmin(f(x)) → unknown
    ans["Q2.5"] = "?"
    return ans

if __name__ == "__main__":
    print("\n======== Q2 ========")
    print(q2())