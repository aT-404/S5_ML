import numpy as np

arr = np.arange(21)
print(f"\nOriginal Array: {arr}")

even_num = arr[arr%2==0]
print(f"\nEven numbers: {even_num}")

great = arr[arr>10]
print(f"\nNumbers greater than 10: {great}")

arr[arr%5==0] = -1
print(f"\nNew array is: {arr}\n\n")