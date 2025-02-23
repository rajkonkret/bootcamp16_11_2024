import numpy as np

arr = np.trunc([-3.16666, 3.66667])
print(arr)  # [-3.  3.]

arr = np.fix([-3.16666, 3.66667])
print(arr)  # [-3.  3.]

arr = np.around(3.1666, 2)
print(arr)  # 3.17

arr = np.floor([-3.16666, 3.66667])
print(arr)  # [-4.  3.]

arr = np.ceil([-3.16666, 3.66667])
print(arr)  # [-3.  4.]

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)  # 24

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)  # 40320

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2], axis=1)
print(x)  # [  24 1680]

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)  # [   5   30  210 1680]

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)  # 12

num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)  # 3

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)  # 4

x = np.sin(np.pi / 2)
print(x)  # 1.0

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
# [1.57079633 3.14159265 4.71238898 6.28318531]

y = np.rad2deg(x)
print(y)  # [ 90. 180. 270. 360.]

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)  # [1 2 3 4 5 6 7]

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(newarr) # [1 2 3 4 5 6]
