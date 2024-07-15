# Length of vector
import numpy as np 
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector

# dot product
import numpy as np 
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result

# multiplication vector and matrix
import numpy as np 
def matrix_multi_vector(matrix, vector):
    result = matrix.dot(vector)
    return result

# Multiplication matrix and matrix
import numpy as np 
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# Inverse matrix
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