import numpy as np

def gauss_jordan(matrix):
    n = len(matrix)
    a = np.array(matrix, dtype=int)

    for i in range(n):
        a[i] = a[i] / a[i][i]

        for j in range(n):
            if j != i:
                a[j] = a[j] - a[j][i] * a[i]

    return a 

n = int(input("Enter the number of equations: "))
matrix = []

print("Enter the augmented matrix row by row (including the constants):")
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

solved_matrix = gauss_jordan(matrix)
print("\nMatrix :")
print(np.round(solved_matrix,))
