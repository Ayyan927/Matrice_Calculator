import numpy as np

A = np.array([
    [2,5,8],
    [8,6,4],
    [2,3,7]
])

B = np.array([
    [1,3,7],
    [6,5,1],
    [3,9,7]
])

print((A@B))
# print(np.dot(A,B))
# print(np.matmul(A,B))a