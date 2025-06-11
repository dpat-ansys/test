#! C:\Users\dpatrizi\.ansys_python_venvs\v_env_test\Scripts\python.exe

import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
array_2 = np.array([6, 7, 8, 9, 10])
my_array = np.concatenate((my_array, array_2))

print(my_array)
print("The shape of the array is:", my_array.shape)
print("The data type of the array is:", my_array.dtype)
