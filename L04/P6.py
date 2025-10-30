import numpy as np

def innerprod(v, u):
    v = np.array(v, dtype=complex)
    u = np.array(u, dtype=complex)
    p = np.dot(v.conj(), u)

    if np.isclose(p.imag, 0):
        return float(p.real)
    else:
        return p

# if __name__ == '__main__':
#     v = np.array([3, 4, 5, 6])
#     u = np.array([1,-1, 0, 2.5])
#     p = innerprod(v, u)
#     print('<v|u> =', p)
#     p = innerprod(u, v)
#     print('<u|v> =', p)
#     v = np.array([3 + 5j, -4j, 0, 1 - 1j, 6 + 9j])
#     u = np.array([2 - 1j, -1.2, 7 + 8j, 3 - 5j, 1.1 + 2j])
#     p = innerprod(v, u)
#     print('<v|u> =', p)
#     p = innerprod(u, v)
#     print('<u|v> =', p)