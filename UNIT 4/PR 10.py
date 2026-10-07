#Practical 10
#Demonstrate NumPy array creation, indexing, slicing, reshaping, broadcasting and mathematical operations on multidimensional
arrays.


import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original Array:")
print(arr)


print("\nIndexing:")
print("Element at [0,1] =", arr[0, 1])
print("Element at [2,2] =", arr[2, 2])


print("\nSlicing:")
print("First two rows:")
print(arr[:2, :])

print("Last two columns:")
print(arr[:, 1:])


a = np.arange(1, 13)
reshaped = a.reshape(3, 4)

print("\nReshaped Array:")
print(reshaped)


b = np.array([10, 20, 30])

print("\nBroadcasting:")
print(arr + b)


print("\nMathematical Operations:")
print("Addition:")
print(arr + 5)

print("Multiplication:")
print(arr * 2)

print("Square:")
print(arr ** 2)

print("Sum =", np.sum(arr))
print("Mean =", np.mean(arr))
print("Maximum =", np.max(arr))
print("Minimum =", np.min(arr))
