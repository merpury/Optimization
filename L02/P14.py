def laplace_smooth(counting, alpha):
    N = sum(counting)
    M = len(counting)
    est_prob = []

    for Ci in counting:
        pi = (Ci + alpha)/(N + alpha*M)
        est_prob.append(pi)

    return est_prob