import numpy as np

arr = np.arange(1,17).reshape(4,4)
print(f"\nThe original array is:\n {arr}")

row = arr[1]
print(f"The second row is: {row}")

col = arr[:,2]
print(f"The third coloumn is: {col}")

n_arr = arr[1:,1:]
print(f"Sub Array:\n {n_arr}")

arr[0] = 0
print(f"New array is:\n {arr}\n\n")