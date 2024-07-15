import numpy as np


def compute_cosine(v1, v2):
    upper = np.dot(v1, v2)
    lower = np.linalg.norm(v1) * np.linalg.norm(v2)
    cos_sim = upper / lower
    return cos_sim


x = np.array([1, 2, 3, 4])
y = np.array([1, 0, 3, 0])
print(compute_cosine(x, y))
