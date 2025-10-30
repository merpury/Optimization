import numpy as np

def marrange(X,Y):
    X = np.ravel(np.array(X))
    Y = np.ravel(np.array(Y))
    Z = X[:, None] * Y

    return Z

# if __name__ == '__main__':
#     X = np.array([1, 2, 3]).reshape((-1,1))
#     Y = np.array([0.5, 1, 5, 10]).reshape((-1,1))
#     Z = marrange(X, Y)    