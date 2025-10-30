import numpy as np
from matplotlib import pyplot as plt
from P9 import Sphere


def trace_ray(O, V, objs, tmin, tmax, BACKGROUND_COLOR=(0,0,0)):

    closest_t = np.inf
    closest_ob = None

    # Loop through all spheres
    for ob in objs:
        t = ob.ray(O, V)

        # print('t =', t)

        if (tmin <= t <= tmax) and (t < closest_t):
            closest_t = t
            closest_ob = ob

    # end for ob

    if closest_ob == None:
        return BACKGROUND_COLOR

    return closest_ob.color


if __name__ == '__main__':

    s1 = Sphere(np.array((0, 0, 80)), 20, (220, 180, 40))
    s2 = Sphere(np.array((0, 150, 400)), 30, (240, 100, 100))
    s3 = Sphere(np.array((50, 100, 200)), 50, (80, 240, 80))
    s4 = Sphere(np.array((100, 50, 300)), 60, (80, 80, 200))
    Geos = [s1, s2, s3, s4]

    # Viewing
    O = np.array((0,0,0))

    VH, VW = 60, 80
    d = 50

    img = np.zeros( (VH, VW, 3), dtype='uint')

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title('Before tracing')
    plt.axis('off')

    # Perform ray tracing

    for i in range(VW):
        for j in range(VH):
            V = np.array((i - VW/2, j - VH/2, d))

            col = trace_ray(O, V, Geos, 0, 1000)
            # print('Color = ', col)

            img[j, i,:] = col

    plt.subplot(1,2,2)
    plt.imshow(img)
    plt.title('After tracing')
    plt.axis('off')

    plt.show()

