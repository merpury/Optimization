import numpy as np
from matplotlib import pyplot as plt

from P7 import plane3d

if __name__ == '__main__':
    n = np.array([1, 1, 1])
    n = n/np.linalg.norm(n)
    k = 3

    xs = np.linspace(-3, 3, 100)
    ys = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(xs, ys)
    Z = plane3d(X, Y, n, k)   

    # Graphics
    fig = plt.figure()

    plt.rcParams['figure.constrained_layout.use'] = True
    plt.rcParams['figure.figsize'] = 6., 6.

    # fig.tight_layout(rect=[0.2, 0.2, 6, 6], h_pad=4, w_pad=4)

    el = 0
    az = -135
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')

    cs = ax1.plot_surface(X, Y, Z, cmap='coolwarm', alpha=1)  # Spicy with color mapping
    ax1.view_init(elev=el, azim=az)
    # ax1.set_title(f'({el},{az})')
    ax1.set_box_aspect((1,1,1))

    # cbar = fig.colorbar(cs, ax=ax1, shrink=0.6)

    # Pointing vector
    ax1.plot([0], [0], [0], 'k*')
    ax1.plot([0, k*n[0]], [0, k*n[1]], [0, k*n[2]], 'r-')

    ax1.set(xlim=(-2, 3), ylim=(-2, 3), zlim=(-1,4),
        xlabel='X', ylabel='Y', zlabel='Z')

    ax1.set_box_aspect((1,1,1))
    ax1.tick_params(axis='both', which='major', labelsize=6)
    ax1.tick_params(axis='both', which='minor', labelsize=6)
    ax1.invert_yaxis()
    ax1.set_title(f'({el},{az},1)')

    els = [0, 0, 5]
    azs = [0, 200, 90]
    for i in range(3):

        el = els[i]
        az = azs[i]

        ax = fig.add_subplot(2, 2, 2+i, projection='3d')

        cs = ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=1)  # Spicy with color mapping
        ax.view_init(elev=el, azim=az)
        ax.set_title(f'({el},{az})')

        # cbar = fig.colorbar(cs, ax=ax1, shrink=0.6)

        # Pointing vector
        ax.plot([0], [0], [0], 'k*')
        ax.plot([0, k*n[0]], [0, k*n[1]], [0, k*n[2]], 'r-')

        ax.set(xlim=(-2, 3), ylim=(-2, 3), #zlim=(-1,4),
        xlabel='X', ylabel='Y', zlabel='Z')

        ax.set_box_aspect((1,1,1))
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.tick_params(axis='both', which='minor', labelsize=6)
        if i > 0:
            ax.invert_yaxis()
        if i in [0,2]:
            ax.invert_xaxis()     

    plt.show()