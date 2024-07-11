import numpy as np
arr = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.nonzero( (arr >=5) & (arr <=10))
print(arr[index])
# 9. Answer C