import tracemalloc
import numpy as np

# tracemalloc.start()
# list1 = list(range(1_000_000))
# list2 = list(range(1_000_000))
#
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
#
# print(f"Current memory usage: {current / 1024 ** 2} MB;")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
# Current memory usage: 76.27836608886719 MB;
# Peak memory usage: 76.27847290039062 MB;

tracemalloc.start()
array1 = np.arange(10_000_000, dtype=np.int8)
array2 = np.arange(10_000_000, dtype=np.int8)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Current memory usage: {current / 1024 ** 2} MB;")
print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
print(f"Array type: {array1.dtype}")
# Current memory usage: 15.25897216796875 MB;
# Peak memory usage: 15.25897216796875 MB;
# Array type: int64
