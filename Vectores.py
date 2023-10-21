from http.client import _DataType
import numpy as np

def gauss_eliminacion(A,b):
    n = len(b)
    # Forward eliminacion
    for i in range(n):
        # Find the pivot row
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]
        #Eliminacion the entries below thr pivot

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]
    # Backward subtitucion
    x= np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[j] /= A[i][i]
    return x

# Example usage:

A = np.array([[1, 1, 1],[2, -1, 1], [3, 2, 1]], dtype=float)
b = np.array([6, 1, 4], dtype=float)
x = gauss_eliminacion(A, b)
print(x)