import numpy as np

class Face:
    def __init__(self, A, B, C, col=(128,128,128)):
        '''
        A, B, C are vertices of the face,
        in order of counter clockwise to the out normal vector.
        Each vertex is a np.array of shape (3,).
        '''
        self.A = A
        self.B = B
        self.C = C
        self.color = col
        # Determine the normal vector
        AB = B - A
        AC = C - A
        self.normal = np.cross(AB, AC)
        norm = np.linalg.norm(self.normal)
        if norm != 0:
            self.normal = self.normal / norm  # Normalize
        else:
            self.normal = np.array([0.0, 0.0, 0.0])  # Degenerate triangle

    def ray(self, O, V):
        # Dummy. Write your code here!
        n = self.normal
        # Step 2. Formulate the plane equation.
        # n.T @ p = k where k = n.T @ A where p is a point on the plane
        k = np.dot(n, self.A)
        denom = np.dot(n, V - O)
        if np.abs(denom) < 1e-8:  # Ray is parallel to the plane
            return np.inf
        # Step 3. Compute the parametric t for the intersection
        t = (k - np.dot(n, O)) / denom
        if t < 0:
            return np.inf
        # Step 4. Determine if the intersection lies
        # within the face boundaries
        # The intersection point Q
        Q = O + t * (V - O)
        AB = self.B - self.A
        BC = self.C - self.B
        CA = self.A - self.C

        AQ = Q - self.A
        BQ = Q - self.B
        CQ = Q - self.C

        if (np.dot(np.cross(AB, AQ), n) >= 0 and
            np.dot(np.cross(BC, BQ), n) >= 0 and
            np.dot(np.cross(CA, CQ), n) >= 0):
            return t 
        else:
            return np.inf
    
# if __name__ == '__main__':
#     f1 = Face(np.array((0, 20, 80)),
#     np.array((-20, -10, 80)),
#     np.array((20, -10, 80)),
#     (240, 200, 100))
#     O = np.array((0,0,0))
#     V1 = np.array((-40, 0, 50))
#     t = f1.ray(O, V1)
#     print('t = {:.3f}'.format(t))
#     V2 = np.array((0, 0, 50))
#     t = f1.ray(O, V2)
#     print('t = {:.3f}'.format(t))