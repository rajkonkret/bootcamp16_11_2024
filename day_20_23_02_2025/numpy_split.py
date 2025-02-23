import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
# [array([1, 2]), array([3, 4]), array([5, 6])]


newarr = np.array_split(arr, 4)

print(newarr)  # [array([1, 2]), array([3, 4]), array([5]), array([6])]
print(newarr[0])  # [1 2]
print(newarr[1])  # [3 4]
print(newarr[2])  # [5]
print(newarr[2])  # [5]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)
print(newarr)
# [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#        [7, 8]]), array([[ 9, 10],
#        [11, 12]])]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]])

newarr = np.array_split(arr, 3, axis=1)
print(newarr)
# [array([[ 1,  2],
#        [ 3,  4],
#        [ 5,  6],
#        [ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [13, 14],
#        [15, 16],
#        [17, 18]]), array([], shape=(9, 0), dtype=int64), array([], shape=(9, 0), dtype=int64)]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)
print(newarr)
# [array([[ 1],
#        [ 4],
#        [ 7],
#        [10],
#        [13],
#        [16]]), array([[ 2],
#        [ 5],
#        [ 8],
#        [11],
#        [14],
#        [17]]), array([[ 3],
#        [ 6],
#        [ 9],
#        [12],
#        [15],
#        [18]])]
