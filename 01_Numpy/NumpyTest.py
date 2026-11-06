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


nums = list(range(1_000_000))
arr  = np.arange(1_000_000)

# Run each 10 times so one slow run doesn't mislead us
t0 = time.perf_counter()
for _ in range(10):
    sum(nums)
list_time = (time.perf_counter() - t0) / 10

t0 = time.perf_counter()
for _ in range(10):
    arr.sum()
numpy_time = (time.perf_counter() - t0) / 10

print(f"list : {list_time:.5f} seconds")
print(f"numpy: {numpy_time:.5f} seconds")
print(f"NumPy is about {list_time / numpy_time:.0f}x faster")


arr = np.array([10, 20, 30, 40])
print(arr)

arr1 = np.array([
    [10.2, 20, 30, 40],
    [2, 4, 8, 9]
])
print(arr1)

arr1 = np.ones((2, 3))
print(arr1)

e = np.linspace(0, 1, 5)     # 5 evenly spaced values from 0 to 1
print(e)

a = np.arange(5, 55, 5)      # start 5, stop before 55, step 5
print(a)


arr1 = np.array([
    [10.2, 20, 30, 40],
    [2, 4, 8, 9]
])

print(arr1.shape)    # (rows, columns)
print(type(arr1))    # it is a NumPy array
print(arr1.dtype)    # float64, because of 10.2

l1 = [2, 3, 4, 5]
print(type(l1))


a = np.arange(5, 55, 5)
print(a)

m = a.reshape(2, 5)    # 10 elements → 2 rows × 5 columns
print(m)


arr = np.array([10, 20, 30, 40])
print(arr[0])     # first
print(arr[-1])    # last

m = np.array([[1, 2, 3],
              [4, 5, 6]])

print(m[1, :])    # row 1 (the second row), all columns


arr2 = np.array([10, 20, 30, 40, 50, 60])
print(arr2[::])    # everything


scores = np.array([45, 82, 67, 91, 38, 74])

mask = scores >= 60
print(mask)            # True where the score is 60 or more
print(scores[mask])    # keep only those scores

scores = np.array([45, 82, 67, 91, 38, 74])

print(scores[(scores >= 60) & (scores < 80)])