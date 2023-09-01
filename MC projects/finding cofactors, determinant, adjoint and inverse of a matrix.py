import numpy as np

M = [[1, 0, 0], [3, 3, 0], [5, 2, -1]]
# finding determinant
determinant = round(np.linalg.det(M))
print(determinant)

# finding inverse
inverse = np.linalg.inv(M)
print(inverse)

# finding adjoint
adjoint = inverse / determinant
print(adjoint)


# finding cofactor of a matrix
def matrix_cofactor(matrix):
    try:
        determinant = np.linalg.det(matrix)
        if determinant != 0:
            cofactor = np.linalg.inv(matrix).T * determinant
            return cofactor
        else:
            raise Exception("singular matrix")
    except Exception as e:
        print("could not find singular matrix as", e)


print(matrix_cofactor(M))
print(np.dot(M, inverse))
