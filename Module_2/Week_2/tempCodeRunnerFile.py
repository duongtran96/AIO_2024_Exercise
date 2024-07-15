import numpy as np
def inverse_matrix(matrix):
    det_matrix = np.linalg.det(matrix)
    if det_matrix!= 0:
        result = np.linalg.inv(matrix)
        print("A invertible \n")
        return result
    else:
        print("Matrix is not invertible \n")

A = np.array([[-2, 6], [8, -4]])
print(inverse_matrix(A))