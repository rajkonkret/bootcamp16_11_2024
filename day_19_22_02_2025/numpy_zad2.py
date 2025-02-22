import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# typ tablicy
print(a.ndim)  # 0
print(b.ndim)  # 1
print(c.ndim)  # 2
print(d.ndim)  # 3 wymiary

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("Wymiar:", arr.ndim)
# [[[[[1 2 3 4]]]]]
# Wymiar: 5

# odczyt indeksu tablicy
print(b)  # [1 2 3 4 5]
print(b[0])  # 1
print(b[2])  # 3

print(c)
# [[1 2 3]
#  [4 5 6]]
print("Pierwszy wiersz: ", c[0])  # [1 2 3]
print("pierwszy wiersz, drugi element:", c[0, 1])  # pierwszy wiersz, drugi element: 2
print(c[0][1])  # 2

arr_10 = np.array(([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
print(arr_10)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
print("Czwarty element, wiersz 2:", arr_10[1, 3])  # Czwarty element, wiersz 2: 9

arr_12_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_12_3d)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

print(arr_12_3d[0])
# [[1 2 3]
#  [4 5 6]]
print(arr_12_3d[0, 1])
# [4 5 6]
print(arr_12_3d[0, 1, 2])  # 6

print(arr_10)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
print("Wiersz indeks 1, ostatni element:", arr_10[1, -1])
