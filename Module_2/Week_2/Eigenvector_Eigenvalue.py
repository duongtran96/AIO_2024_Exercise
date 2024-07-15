import numpy as np
from numpy.linalg import eig


def compute_eigenvalues_eigenvectors(matrix):
    inity_matrix = np.array([[1, 0], [0, 1]])
    delta = (matrix[0, 0] + matrix[1, 1]) ** 2 - 4 * \
        (matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0])
    eigenvalues = []
    if delta < 0:
        print("matrix not eigenvalue")
    elif delta == 0:
        eigenvalues = - (matrix[0, 0] + matrix[1, 1]) / 2
    else:
        eigenvalue_1 = ((matrix[0, 0] + matrix[1, 1]) - np.sqrt(delta)) / 2
        eigenvalue_2 = ((matrix[0, 0] + matrix[1, 1]) + np.sqrt(delta)) / 2
        eigenvalues = [np.round(eigenvalue_1, 2), np.round(eigenvalue_2, 2)]

    # eigenvectors
    # for eigenvalue_1
        vector_1 = np.subtract(matrix, eigenvalues[0] * inity_matrix)
        eigenvector_1 = np.array([1, (-vector_1[0, 1] / vector_1[0, 0])])
        norm_eigenvector_1 = np.linalg.norm(eigenvector_1)
        eigenvector_1 = eigenvector_1 / norm_eigenvector_1

    # for eigenvalue_2
        vector_2 = np.subtract(matrix, eigenvalues[1] * inity_matrix)
        eigenvector_2 = np.array([1, (-vector_2[0, 1] / vector_2[0, 0])])

        norm_eigenvector_2 = np.linalg.norm(eigenvector_2)

        eigenvector_2 = np.array([eigenvector_2 / norm_eigenvector_2])

    return eigenvalues, eigenvector_1, eigenvector_2


A = np.array([[0.9, 0.2], [0.1, 0.8]])
out = compute_eigenvalues_eigenvectors(A)
print(out)
