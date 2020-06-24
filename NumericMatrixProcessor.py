from typing import List, Any


class Matrix:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        for _i in range(rows):
            self.matrix.append([])
            self.matrix[_i] = list(map(float, input().split()[:columns]))


def determinant(matrix):
    det = 0
    if len(matrix) == len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - \
               matrix[0][1] * matrix[1][0]
    if len(matrix) == len(matrix[0]) == 1:
        return matrix[0][0]
    for i in range(len(matrix[0])):
        det += matrix[0][i] * pow(-1, (1 + i + 1)) * determinant(minor(matrix, 0, i))
    return det


def cofactor(matrix):
    cof = []
    if len(matrix) == len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - \
               matrix[0][1] * matrix[1][0]
    if len(matrix) == len(matrix[0]) == 1:
        return matrix[0][0]
    for i in range(len(matrix)):
        cof.append([])
        for j in range(len(matrix[0])):
            cof[i].append(pow(-1, (i + 1 + j + 1)) * determinant(minor(matrix, i, j)))
    return cof


def minor(matrix, row_i, col_i):
    minor_m = [row[:] for row in matrix]
    for row in minor_m:
        del row[col_i]
    del minor_m[row_i]
    return minor_m


def add_matrix():
    sum_matrix = []
    if matrixA_dim == matrixB_dim:
        for i in range(matrixA.rows):
            sum_matrix.append([])
            for j in range(matrixA.columns):
                sum_matrix[i].append(matrixA.matrix[i][j] +
                                     matrixB.matrix[i][j])
        return sum_matrix

    else:
        print("ERROR")


def multiply(matrix, number):
    mult_matrix = []
    for i in range(len(matrix)):
        mult_matrix.append([])
        for j in range(len(matrix[0])):
            mult_matrix[i].append(round(matrix[i][j] * number, 3))
    return mult_matrix


def matrix_multiplication():
    if matrixA.columns == matrixB.rows:
        result: List[List[Any]] = []
        for i in range(matrixA.rows):
            result.append([])
            for j in range(matrixB.columns):
                result[i].append(0)
                for k in range(matrixB.rows):
                    result[i][j] += round(matrixA.matrix[i][k] * matrixB.matrix[k][j], 3)
        return result

    else:

        print("The operation cannot be performed.")


def matrix_transposition(matrix, choice1):
    transposed = []
    columns = len(matrix[0])
    rows = len(matrix)
    if choice1 == 1:

        for i in range(columns):
            transposed.append([])
            for k in range(rows):
                transposed[i].append(matrix[k][i])

    if choice1 == 2:

        for i in range(columns):
            # create the empty list
            transposed.append([])
            # range through the rows and append every column starting from
            # the last element
            for j in range(rows - 1, -1, -1):
                transposed[i].append(matrix[j][-1 - i])

    if choice1 == 3:
        for i in range(rows):
            transposed.append([])
            for j in range(columns - 1, -1, -1):
                transposed[i].append(matrix[i][j])

    if choice1 == 4:
        transposed = matrix[::-1]

    return transposed


def inverse(matrix):
    if len(matrix) == 2 or determinant(matrix) == 0:
        return True
    else:
        transposed = matrix_transposition(cofactor(matrix), 1)
        return multiply(transposed, 1 / determinant(matrix))


while True:

    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n"
          "4. Transpose matrix\n5. Calculate a determinant\n6. Inverse Matrix\n0. Exit")
    choice = int(input("Your choice > "))

    if choice == 1:
        matrixA_dim = [int(x) for x in input("Enter size of first matrix").split()]
        print("Enter first matrix :")
        matrixA = Matrix(matrixA_dim[0], matrixA_dim[1])
        matrixB_dim = [int(x) for x in input("Enter size of second matrix").split()]
        print("Enter second matrix :")
        matrixB = Matrix(matrixB_dim[0], matrixB_dim[1])
        print("The result is:")
        for _row in add_matrix():
            print(*_row)
    elif choice == 2:
        matrixA_dim = [int(x) for x in input("Enter size of the matrix: ").split()]
        print("Enter matrix :")
        matrixA = Matrix(matrixA_dim[0], matrixA_dim[1])
        constant = float(input("Enter constant:"))
        print("The result is:")
        for _row in multiply(matrixA.matrix, constant):
            print(*_row)
    elif choice == 3:
        matrixA_dim = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix: ")
        matrixA = Matrix(matrixA_dim[0], matrixA_dim[1])
        matrixB_dim = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter second matrix:")
        matrixB = Matrix(matrixB_dim[0], matrixB_dim[1])
        if matrix_multiplication():
            print("The result is:")
            for _row in matrix_multiplication():
                print(*_row)
    elif choice == 4:
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        choice = int(input("Your choice > "))
        matrixA_dim = [int(x) for x in input("Enter size of the matrix: ").split()]
        print("Enter matrix: ")
        matrixA = Matrix(matrixA_dim[0], matrixA_dim[1])
        print("The result is:")
        for _row in matrix_transposition(matrixA.matrix, choice):
            print(*_row)
    elif choice == 5:
        matrixA_dim = [int(x) for x in input("Enter size of the matrix: ").split()]
        print("Enter matrix: ")
        matrixA = Matrix(matrixA_dim[0], matrixA_dim[1])
        print("The result is:\n", determinant(matrixA.matrix), sep="")
    elif choice == 6:
        matrixA_dim = [int(x) for x in input("Enter size of the matrix: ").split()]
        print("Enter matrix: ")
        matrixA = Matrix(matrixA_dim[0], matrixA_dim[1])
        print("The result is:")
        for _row in inverse(matrixA.matrix):
            print(*_row)
        print("")
    elif choice == 0:
        break
