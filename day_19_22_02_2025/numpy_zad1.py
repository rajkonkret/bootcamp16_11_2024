import numpy as np

# pip  install numpy

print(np.__version__)  # 2.1.3

arr = np.array([1, 2, 3, 4, 5])

print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>

# 0-D
arr_0d = np.array(42)
print(arr_0d)  # 42
print(type(arr_0d))  # <class 'numpy.ndarray'>

# 1-D
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)  # [1 2 3 4 5]

# 2-D
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]

# 3-D
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_3d)
# [[[1 2 3]
#   [4 5 6]]
#
#  [[1 2 3]
#   [4 5 6]]]
