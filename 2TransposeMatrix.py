import numpy as np

def transpose(matrix):
    return np.transpose(matrix)

matrix = np.array([[1,2],[3,4]])

result = transpose(matrix)
print(result)