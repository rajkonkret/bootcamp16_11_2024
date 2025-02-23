import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
# [1 2 3]
# [4 5 6]

for x in arr:
    print(x)
    for y in x:
        print(y)
# [1 2 3]
# 1
# 2
# 3
# [4 5 6]
# 4
# 5
# 6

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

for x in np.nditer(arr):
    print(x)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
# np.bytes_(b'1')
# np.bytes_(b'2')
# np.bytes_(b'3')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)
# 1
# 3
# 5
# 7

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
# (0,) 1
# (1,) 2
# (2,) 3

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)
# (0, 0) 1
# (0, 1) 2
# (0, 2) 3
# (0, 3) 4
# (1, 0) 5
# (1, 1) 6
# (1, 2) 7
# (1, 3) 8
