import numpy as np

def create_polynomial_features(X, degree = 2):
    """ Create the polynomial features
    Args:
        X: A array tensor for the data
        degree: A integer for the degree 
        of the generated polynomail fuction
    """
    X_new = X 
    for d in range(2, degree + 1):
        X_new = np.c_[X_new, np.power(X_new, d)]
    
    return X_new

def create_polynomial_features_2(X, degree = 2):
    """ Creates the polynomial features
    Args :
    X : A array for the data .
    degree : A intege for the degree of
    the generated polynomial function .
    """
    X_mem = []
    for X_sub in X.T :
        X_new = X_sub
        for d in range (2 , degree +1) :
            X_new = np.c_[ X_new,np.power(X_sub , d)]
            X_mem.extend(X_new.T)
    return np.c_[X_mem].T


if __name__ == "__main__":
    # X = np.array([[1], [2], [3]])
    # degree = 2
    # print(create_polynomial_features(X, degree))

    X = np.array([[1, 2], [2, 3], [3, 4]])
    degree = 2
    print(create_polynomial_features_2(X, degree))