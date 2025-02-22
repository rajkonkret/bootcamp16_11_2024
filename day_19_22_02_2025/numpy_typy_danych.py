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

arr_float_2 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(arr_float_2.dtype)
print(arr_float_2)
# float64
# [1.1 2.2 3.3 4.4 5.5]
print('Konwwersja na int32', arr_float_2.astype("int32"))
print('Konwwersja na int32', arr_float_2.astype("int32").dtype)
# Konwwersja na int32 [1 2 3 4 5]
# Konwwersja na int32 int32

print('Konwwersja na float16', arr_float_2.astype("float16"))
print('Konwwersja na float16', arr_float_2.astype("float16").dtype)
# Konwwersja na float16 [1.1 2.2 3.3 4.4 5.5]
# Konwwersja na foat16 float16

print('Konwwersja na bool', arr_float_2.astype("bool"))
print('Konwwersja na bool', arr_float_2.astype("bool").dtype)
# Konwwersja na bool [ True  True  True  True  True]
# Konwwersja na bool bool

print('Konwwersja na U6', arr_float_2.astype("U6"))
print('Konwwersja na U6', arr_float_2.astype("U6").dtype)
# Konwwersja na U6 ['1.1' '2.2' '3.3' '4.4' '5.5']
# Konwwersja na U6 <U6 unicode długości 6

print('Konwwersja na uint8', arr_float_2.astype("uint8"))
print('Konwwersja na uint8', arr_float_2.astype("uint8").dtype)
# Konwwersja na uint8 [1 2 3 4 5]
# Konwwersja na uint8 uint8
