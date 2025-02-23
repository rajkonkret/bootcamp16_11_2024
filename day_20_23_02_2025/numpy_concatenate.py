import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)  # [1 2 3 4 5 6]

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1)
print(arr2)
# [[1 2]
#  [3 4]]
# [[5 6]
#  [7 8]]
arr = np.concatenate((arr1, arr2))
print(arr)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
# [[1 2 5 6]
#  [3 4 7 8]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack([arr1, arr2], axis=1)
print(arr)
# [[1 4]
#  [2 5]
#  [3 6]]
arr = np.stack([arr1, arr2])
print(arr)
# [[1 2 3]
#  [4 5 6]]
arr = np.hstack([arr1, arr2])
print(arr) # [1 2 3 4 5 6]

arr = np.vstack([arr1, arr2])
print(arr)
# [[1 2 3]
#  [4 5 6]]

arr = np.dstack([arr1, arr2])
print(arr)
# [[[1 4]
#   [2 5]
#   [3 6]]]
print(arr.shape) # (1, 3, 2)