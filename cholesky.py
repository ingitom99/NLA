"""
CHOLESKY
"""

# Imports
from numpy import zeros

def cholesky(A):
    """ Compute the Cholesky factor, L, of SPD square numpy array A"""
    L = zeros(A.shape)
    for j in range(A.shape[0]):
        L[j][j] = A[j][j]
        for k in range(j-1):
            L[j][j] -= L[j][k]**2
        if L[j][j] < 0:
            print("A is not SPD!!!")
            return None
        L[j][j] = L[j][j]**.5
        for i in range(j+1, A.shape[0]):
            L[i][j] = A[i][j]
            for k in range(j-1):
                L[i][j] -= L[i][k] * L[j][k]
            L[i][j] *= 1/L[j][j]
    return L
