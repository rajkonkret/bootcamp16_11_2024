import numpy as np

lista = [1, 2, 3, 4, 5]
print(lista[2:4])  # [3, 4]
# [start:stop]

# indexy        0  1  2  3  4  5  6
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # [2 3 4 5]
print(arr[4:])  # [5 6 7] od indeksu 4 do końća
print(arr[:4])  # [1 2 3 4] bez indeksu 4
print(arr[-3:-1])  # [5 6]

# [start:stop:step]
print(arr[1:5:2])  # [2 4], krok=2
print(arr[::2])  # [1 3 5 7]

arr_10_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_10_2d)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
print("Wiersz indeks 1(czyli2), element indeks 4 (czyli 5) ", arr_10_2d[1, 1:4])
# Wiersz indeks 1(czyli2), element indeks 4 (czyli 5)  [7 8 9]
print(arr_10_2d[0:2, 2])
# [3 8] z wierszy z zakresu 0:2 (u nas 0,1) wyciąga element o indeksie 2
# zwrócił listę z elementem 2 we wszystkich wierszach

print(arr_10_2d[0:2, 1:4])
# [[2 3 4]
#  [7 8 9]]

array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
print(array_3d)
print(array_3d[0])
# [[1 2 3]
#  [4 5 6]]
print(array_3d[0:2, 1:2, 0:1])
# [[[ 4]]
#
#  [[10]]]