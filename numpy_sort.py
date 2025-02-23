import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))  # [0 1 2 3]

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))  # ['apple' 'banana' 'cherry']

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
# [[2 3 4]
#  [0 1 5]]
