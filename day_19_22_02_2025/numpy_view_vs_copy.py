# Widok (View) - odwzorowanie danych z tabeli
# zmiana danych w widoku zmienia dane w tabeli
# umożliwia częściową reprezentację danych z tabeli
import numpy as np

# kopia tabeli
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
# [42  2  3  4  5]
# [1 2 3 4 5]
print(id(x), id(arr))  # 2627311068016 2627275941104
print(x.base is arr)  # False - nie jest widokiem

# widok
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
# [42  2  3  4  5]
# [42  2  3  4  5]
print(id(x), id(arr))  # 1672226563312 1672259658992
print(x.base is arr)  # True jest widokiem

arr = np.arange(10)
view = arr[2:5]  # taki slice zwraca widok
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
print(view)  # [2 3 4]
view[0] = 99
print(arr)
print(view)
# [ 0  1 99  3  4  5  6  7  8  9]
# [99  3  4]
print(view.base is arr)  # True

arr = np.arange(10)
copy = arr[::2]
copy[0] = 99
print(copy)
print(arr)
print(copy.base in arr)  # True

arr = np.arange(1000)
copy = arr[::2]
copy[0] = 99
print(copy)
print(arr)
print(copy.base in arr)  # True

arr = np.arange(1, 13).reshape(3, 4)
print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

view_col = arr[:, 1].view()
print(view_col)  # [ 2  6 10]
view_col[:] = 99
print(arr)
# [[ 1 99  3  4]
#  [ 5 99  7  8]
#  [ 9 99 11 12]]

copy_row = arr[0, :].copy()
copy_row[:] = 0
print(arr)
print(copy_row)
# [[ 1 99  3  4]
#  [ 5 99  7  8]
#  [ 9 99 11 12]]
# [0 0 0 0]
print(copy_row.base is arr)  # False

view_submatrix = arr[:2, :2].view()
view_submatrix *= 10
print(view_submatrix)
# [[ 10 990]
#  [ 50 990]]
print(arr)
# [[ 10 990   3   4]
#  [ 50 990   7   8]
#  [  9  99  11  12]]
lista = [1, 2, 3, 4, 5]
# print(lista * 2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
lista_slice = lista[1:3]
print(lista_slice)
lista_slice[0] = 99
print(lista_slice)
print(lista)
# [99, 3]
# [1, 2, 3, 4, 5]

arr_1d = np.arange(10)
view_reversed = arr_1d[::-1].view()
view_reversed[0] = 999
print(arr_1d)
print(view_reversed)
# [  0   1   2   3   4   5   6   7   8 999]
# [999   8   7   6   5   4   3   2   1   0]
print(view_reversed.base is arr_1d)  # True

arr_3d = np.arange(27).reshape((3, 3, 3))
copy_3d = arr_3d.copy()
copy_3d[0, 0, 0] = -1
print(arr_3d)
print(copy_3d)
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
#
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]
# [[[-1  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
#
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]

arr_float = np.array([1.1, 2.2, 3.3, 4.4], dtype='float32')
print(arr_float.dtype)  # float32
# stworzyło kopię
arr_view_as_int = arr_float.astype('int32').view()
print(arr_float)
print(arr_view_as_int)
# [1.1 2.2 3.3 4.4]
# [1 2 3 4]
print(arr_float.dtype)
print(arr_view_as_int.dtype)
# float32
# int32
print(arr_view_as_int.base is arr_float)  #
