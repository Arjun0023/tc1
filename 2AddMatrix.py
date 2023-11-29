import numpy as np

def add(matrix1,matrix2):
    return np.add(matrix1,matrix2)

matrix1 = np.array([[1,2],[2,3]])
matrix2 = np.array([[1,2],[2,3]])

result = add(matrix1,matrix2)
print(result)