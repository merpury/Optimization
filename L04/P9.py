import numpy as np

class Sphere:
    def __init__(self, C, r, col=(128,128,128)):
        self.C = C
        self.r = r
        self.color = col

    def ray(self, O, V):
        OC = O - self.C
        a = np.dot(V - O, V - O)
        b = 2 * np.dot(OC, V - O)
        c = np.dot(OC, OC) - self.r**2

        discriminant = b**2 - 4*a*c

        if discriminant < 0:
            return np.inf
        else:
            sqrt_disc = np.sqrt(discriminant)
            t1 = (-b - sqrt_disc) / (2*a)
            t2 = (-b + sqrt_disc) / (2*a)

        return min(t1, t2)

if __name__ == '__main__':
    s1 = Sphere(np.array((0, 0, 80)), 20, (220, 180, 40))
    O = np.array((0,0,0))
    V1 = np.array((-40, 0, 50))
    t = s1.ray(O, V1)
    print('t = {:.3f}'.format(t))
    V2 = np.array((0, 0, 50))
    t = s1.ray(O, V2)
    print('t = {:.3f}'.format(t))
    V3 = np.array((10, 0, 50))
    t = s1.ray(O, V3)
    print('t = {:.3f}'.format(t))