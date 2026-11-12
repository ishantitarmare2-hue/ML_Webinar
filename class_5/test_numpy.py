import numpy as np

print(np.__version__)

a = np.array([10, 20, 30])
a=a+5
print(a)

a = np.array([10, 20, 30])
print(a.shape)
print(a.reshape(3, 1))

a = np.array([10, 20, 30])
print(a.shape)
print(a.reshape(3, 1)+np.array([0, 1, 2]))

a = np.array(12).reshape(3, 4)
print(a)