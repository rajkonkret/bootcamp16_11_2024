# brodcasting
# zamienia elementy tablicy wg podanego wzoru automatycznie,
# nie trzeba ręcznie na każdym elemencie tej operacji wykonywac
# jesli wymiary są równe jest ok
# jesli jeden z wymiarów wynosi 1, NumPy rozciąga ten wymiar aby dopassowac do drugiej tablicy
# jesli wymiary się róznią i zaden nie wynosi 1 to mamy bład
import numpy as np

arr = np.array([1, 2, 3])
result = arr + 10  # 10 -> wymiar (1,) -> [10 10 10]
print(result)  # [11 12 13]

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
print(arr1)  # wymiar(3,)
print(arr2)  # wymiar (3,1)
result = arr1 + arr2
# [1 2 3]
# [[10]
#  [20]
#  [30]]
# [[10 10 10]
#  [20 10 10]
#  [30 30 30]]
print(result)
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

arr1 = np.array(([[1, 2, 3], [4, 5, 6]]))
arr2 = np.array([10, 20, 30])
result = arr1 + arr2
print(result)
# [[11 22 33]
#  [14 25 36]]

arr1 = np.ones((4, 3, 2))
print(arr1)
# [[[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]]
arr2 = np.array([10, 20])  # (2,)
result = arr1 + arr2
print(result)
#  [[11. 21.]
#   [11. 21.]
#   [11. 21.]]
#
#  [[11. 21.]
#   [11. 21.]
#   [11. 21.]]
#
#  [[11. 21.]
#   [11. 21.]
#   [11. 21.]]]

arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20])
# result = arr1 + arr2
# ValueError: operands could not be broadcast together with shapes (3,) (2,)
#
# x = np.arange(5)
# y = np.arange(3)
# print(x + y) # ValueError: operands could not be broadcast together with shapes (5,) (3,)

x = np.arange(5)
y = np.arange(3).reshape(3, 1)
print(x)
print(y)
print(x + y)
# [[0 1 2 3 4]
#  [1 2 3 4 5]
#  [2 3 4 5 6]]

print(np.zeros((3, 3)))
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
