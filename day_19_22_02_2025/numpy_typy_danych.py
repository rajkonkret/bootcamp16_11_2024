# int8 - liczby całkowite na 8 bitach - > -128 do 127
# uint8 - int bez znaku -> 0 do 255
# int16 - -32768 do 32767
import numpy as np

arr = np.array([1, 2, 3, 4])
# odczytanie typu danch
print(arr.dtype)  # int64

# Minimalna wartość int64: -9223372036854775808
# Maksymalna wartość int64: 9223372036854775807
print(np.iinfo(np.int64).min)
print(np.iinfo(np.int64).max)
# -9223372036854775808
# 9223372036854775807

arr_str = np.array(['apple', 'banana', 'cherry'])
print(arr_str.dtype)  # <U6 unicode string, długość 6

# stworzenie listy określonego typu
arr_own = np.array([1, 2, 3, 4], dtype="S")
print(arr_own.dtype)
print(arr_own)
# |S1
# [b'1' b'2' b'3' b'4']

arr_4i = np.array([1, 2, 3, 4], dtype='i4')
print(arr_4i)
print(arr_4i.dtype)
# [1 2 3 4]
# int32

#     arr_err = np.array(['a', "2", "3"], dtype="i")
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'a'
# arr_err = np.array(['a', "2", "3"], dtype="i")
# print(arr_err)

arr_float = np.array([1.1, 2.1, 3.1, 4.1])
print(arr_float)
print(arr_float.dtype)
# [1.1 2.1 3.1 4.1]
# float64
newarr = arr.astype("i")
print(newarr)
print(newarr.dtype)
# [1 2 3 4]
# int32

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
# [1 2 3 4]
# int64

arr_bool = np.array(([1, 0, 3]))
new_arr_bool = arr_bool.astype(bool)

print(new_arr_bool)
print(new_arr_bool.dtype)
# [ True False  True]
# bool