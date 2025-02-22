import numpy as np

arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
print(arr.dtype)  # int64

arr = np.arange(5, 23)
print(arr)
print(arr.dtype)
# [ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22]
# int64

arr = np.arange(0, 20, 2)
print(arr)  # [ 0  2  4  6  8 10 12 14 16 18]

arr = np.arange(10, 0, -1)
print(arr)  # [10  9  8  7  6  5  4  3  2  1]

arr = np.arange(0, 1, 0.1)
print(arr)  # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

arr = np.arange(0, 5, dtype="float32")
print(arr)
print(arr.dtype)
# [0. 1. 2. 3. 4.]
# float32

arr = np.arange(1, 5, dtype="complex")
print(arr)
print(arr.dtype)
# [1.+0.j 2.+0.j 3.+0.j 4.+0.j]
# complex128


arr = np.arange(0, 5, 0.5)
print(arr)
print(arr.dtype)
# [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
# float64

arr = np.linspace(0, 1, 10)
print(arr)
# [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
#  0.66666667 0.77777778 0.88888889 1.        ]

arr = np.linspace(0, 1, num=10, endpoint=False)
print(arr)  # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

arr, step = np.linspace(0, 1, num=5, retstep=True)
print('Tablica: ', arr)
print("Krok", step)
# Tablica:  [0.   0.25 0.5  0.75 1.  ]
# Krok 0.25

print(arr.shape)  # (5,) 5 elementów w jwdnym wierszu

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
print(arr.shape)
# [[1 2 3 4]
#  [5 6 7 8]]
# (2, 4) dwa wiersze, 4 elementy

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.shape)  # (1, 1, 1, 1, 4)
