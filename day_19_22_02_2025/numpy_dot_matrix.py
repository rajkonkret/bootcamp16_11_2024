from typing import List, Tuple
import time
import random

import numpy as np

PythonArray2D = List[List[float]]

def multiply_python_arrays(x: PythonArray2D,
                           y: PythonArray2D) -> PythonArray2D:
    result = initialize_array_2D(
        shape=(len(x), len(y[0]))
    )
    for i in range(len(x)):
        for j in range(len(y[0])):
            dot_product =0
            for k in range(len(x[0])):
                dot_product += x[i][k] * y[k][j]
            result[i][j] = dot_product
    return result

def generate_random_array2D(shape: Tuple[int,int]) -> PythonArray2D:
    result = initialize_array_2D(shape=shape)
    for row in range(shape[0]):
        for col in range(shape[1]):
            result[row][col] = random.random()
    return result

def initialize_array_2D(shape: Tuple[int, int]) -> PythonArray2D:
    return [
        [0.0 for _ in range(shape[1])]
        for _ in range(shape[0])
        ]


PYTHON_ARRAY_A = generate_random_array2D(shape=[200, 300])
PYTHON_ARRAY_B = generate_random_array2D(shape=[300, 200])

NUMPY_ARRAY_A  = np.array(PYTHON_ARRAY_A)
NUMPY_ARRAY_B  = np.array(PYTHON_ARRAY_B)

start_time = time.time()
python_operation_result  =multiply_python_arrays(x=PYTHON_ARRAY_A, y=PYTHON_ARRAY_B)
python_exec_time = time.time() - start_time
print(f"Time: {python_exec_time}")

start_time = time.time()
numpy_operation_result = NUMPY_ARRAY_A.dot(NUMPY_ARRAY_B)
numpy_exec_time = time.time() - start_time
print(f"Time: {numpy_exec_time}")

print(python_exec_time / numpy_exec_time)

result_diff = np.sum(np.absolute(numpy_operation_result - np.array(python_operation_result)))
print(result_diff)
print(result_diff < 1e5)

Time: 1.6792140007019043
Time: 0.009407758712768555
178.49246052864999
1.1903011909453198e-09
True
