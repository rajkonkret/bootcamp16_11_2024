from pprint import pprint

import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]

newarr = arr[x]
print(newarr)  # [41 43]

arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)  # [False, False, True, True]
print(newarr)  # [43 44]

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42

newarr = arr[filter_arr]
print(filter_arr)  # [False, False, True, True]
print(newarr)
# [False False  True  True]
# [43 44]

arr = np.arange(21)
even = arr[arr % 2 == 0]
print("Liczby parzyste:", even)
# Liczby parzyste: [ 0  2  4  6  8 10 12 14 16 18 20]

arr = np.random.randint(0, 10, size=100)

mean_value = np.mean(arr)
greather_than_mean = arr[arr > mean_value]
print("Srednia:", mean_value)  # Srednia: 4.4
print("Wartości większe od średniej:", greather_than_mean)
# Wartości większe od średniej: [7 5 8 8 6 5 5 9 6 6 5 5 9 7
# 5 9 6 6 8 9 9 9 8 5 7 5 9 6 7 5 7 9 8 7 9 9 7
#  9 9 8 5 5 5 5 7 9 5]

arr = np.array([1, 2, np.nan, 4, np.nan, 6, 7])

filtered_arr = arr[~np.isnan(arr)]
print("Tablica bez NaN:", filtered_arr)  # Tablica bez NaN: [1. 2. 4. 6. 7.]

arr = np.random.random((5, 5))
print(arr)
print(arr.shape)  # (5, 5)

filtered_arr = arr[arr > 0.5]
print("Większe od 0.5:", filtered_arr)
# Większe od 0.5: [0.72241326 0.85903952 0.94030393 0.52205497 0.52297721 0.99057821
#  0.75381307 0.89526586 0.64877792 0.77154062 0.58929343 0.75113094
#  0.67649512 0.72409597]
print(filtered_arr.shape)  # (9,)

fruits = np.array(['jabłko', 'banan', 'wiśnia', 'gruszka', 'kiwi'])

filtered_fruits = fruits[np.char.find(fruits, 'a') >= 0]
print("Owoce zawierające literę a:", filtered_fruits)
# Owoce zawierające literę a: ['jabłko' 'banan' 'wiśnia' 'gruszka']

arr = np.arange(20)

filtered_arr = arr[np.arange(len(arr)) % 2 == 0]
print("Wartości na parzystych indeksach:", filtered_arr)
# Wartości na parzystych indeksach: [ 0  2  4  6  8 10 12 14 16 18]

mask = np.arange(len(arr)) % 2 == 0
print("Maska filtrowania:", mask)
# Maska filtrowania: [ True False  True False  True False  True False  True False  True False
#   True False  True False  True False  True False]

arr = np.array([1, 2, np.nan, 4, np.inf, 6, -np.inf, 8])
# np.inf - wartość nieskońćzona
print(arr)
# filtered_arr = arr[np.isinf(arr)]
# filtered_arr = arr[np.isnan(arr)] # [nan]
filtered_arr = arr[np.isfinite(arr)]  # bez NaN i bez inf
print(filtered_arr)
# [1. 2. 4. 6. 8.]

# zamieniło nan i inf na 0
sanitized_arr = np.where(np.isfinite(arr), arr, 0)
print(sanitized_arr)  # [1. 2. 0. 4. 0. 6. 0. 8.]
