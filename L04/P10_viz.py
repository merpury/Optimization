import numpy as np
from matplotlib import pyplot as plt
# from P9 import Sphere
from P10 import Face


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

    # s1 = Sphere(np.array((0, 0, 80)), 20, (220, 180, 40))
    # s3 = Sphere(np.array((50, 100, 200)), 50, (80, 240, 80))
    f1 = Face(np.array((30, 40, 90)), 
            np.array((10, 10, 100)),
            np.array((50, 10, 200)),
            (80, 80, 200))

    f2 = Face(np.array((-40, -40, 90)), 
            np.array((0, 0, 90)),
            np.array((-40, 40, 200)),
            (240, 100, 100))

    f3 = Face(np.array((0, 20, 80)), 
            np.array((-20, -10, 80)),
            np.array((20, -10, 80)),
            (240, 200, 100))

    # Geos = [s1, s3, f1, f2]
    Geos = [f1, f2, f3]


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

