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

a = np.arange(12).reshape(3, 4)
print(a)
print(a.mean(axis=1))

m = np.arange(12).reshape(3, 4)
print(m)
print("____________________________")
print(m.mean(axis=0))
print("____________________________")

a = np.array([10, 20, 30, 26, 27, 12, 9 ])
req_val=np.where(a>15,1,0)
print(req_val)

rng = np.random.default_rng(42)
print(rng.integers(0, 100, 5))

rng = np.random.default_rng(42)
print(rng.integers(0, 100, 5))