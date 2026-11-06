import numpy as np

# arr1 = np.arange (5 ,55 ,5)
# print(arr1)

# arr2 = arr1.reshape(2,5)
# print(arr2)
# print(arr2.shape)
# print(arr2.dtype)
# print(arr2.ndim)


marks = np.array([45, 82, 67, 91, 38, 74, 59, 88])
print(marks[marks >= 60])
print(marks[marks >= 60].mean())
print(marks[( marks >= 60) & (marks <= 80)])