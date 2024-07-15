import numpy as np
arr = np.arange(0, 10 , 1)
print(arr)
# 1: Answer A

import numpy as np
arr_1 = np.full((3, 3),fill_value = True, dtype = bool)
print(arr_1)
arr_2 = np.ones((3, 3)) > 0
print(arr_2)
arr_3 = np.ones((3, 3)) > 0
print(arr_3)
# 2. Answer D

import numpy as np
arr = np.arange(0, 10)
print(arr[arr %2 ==1])
# 3. Answer A

import numpy as np
arr = np.arange(0, 10)
arr[arr %2 == 1] = -1
print(arr)
# 4. Answer B

import numpy as np
arr = np.arange(10)
arr_2D = arr.reshape(2, -1)
print(arr_2D)
# 5. Answer B

import numpy as np
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2],axis = 0)
print(c)
# 6. Answer A

import numpy as np
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2],axis = 1)
print(c)
# 7. Answer C: axis = 0.
# concatenate: axis = 0: Merge by row, axis = 1 : merge by columns

import numpy as np
arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))
# 8. Answer A

import numpy as np
arr = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.nonzero( (arr >=5) & (arr <=10))
print(arr[index])
# 9. Answer C

import numpy as np
def maxx(x, y):
    if x >= y :
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes = [float])
print(pair_max(a, b))
# 10. Answer D

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print(np.where(a < b, b, a))
# 11. Answer A