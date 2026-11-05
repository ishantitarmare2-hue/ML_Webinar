import numpy as np
import time

nums = list(range(1_000_000))

total  = 0
for num in nums:
    total += num
print(total)


num = [list(range(100000))]
arr=np.arange(100000)
print(num)
print(arr)


nums = list(range(1_000_000))
arr = np.arange(1_000_000)

t0 = time.time()
sum(nums)
print("list :", time.time() - t0)
t0 = time.time() 
np.sum(arr)
print("numpy :", time.time() - t0)   


arr = np.array([10,20,30,40])
print(arr[-1])


arr1 = np.ones((2,3))
print(arr1)


e = np.linspace(0, 1, 5)
print(e)