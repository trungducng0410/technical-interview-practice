# Brute force: Loop through each element, zero col and row from 0 -> Set all elements to 0
# BCR: O(m * n)


# Time complexity: O(n^2)
# Space complexity: O(n)
def zeroMatrix(matrix):
    cols = []
    rows = []

    # O(n^2)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    # Zero out rows
    for row in rows:
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    # Zero out cols
    for i in range(len(matrix)):
        for col in cols:
            matrix[i][col] = 0

    return matrix


# Time complexity: O(n^3)
# Space complexity: O(1)
def zeroMatrixInplace(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = None

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == None:
                for col in range(n):
                    if matrix[i][col] != None:
                        matrix[i][col] = 0

                for row in range(m):
                    if matrix[row][j] != None:
                        matrix[row][j] = 0

                matrix[i][j] = 0

    return matrix


# Time complexity: O(n^2)
# Space complexity: O(1)
def zeroMatrixOptimal(matrix):
    m, n = len(matrix), len(matrix[0])

    firstRowHasZero = False
    for j in range(n):
        if matrix[0][j] == 0:
            firstRowHasZero = True
            break

    firstColHasZero = False
    for i in range(m):
        if matrix[i][0] == 0:
            firstColHasZero = False
            break

    # Store row index and col index should nullify in first col and row
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # Nullify col
    for j in range(n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0

    # Nullify row
    for i in range(m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0

    # Nullify first col if needed
    if firstColHasZero:
        for i in range(m):
            matrix[i][0] = 0

    # Nullify first row if needed
    if firstRowHasZero:
        for j in range(n):
            matrix[0][j] = 0

    return matrix


print(zeroMatrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))
print(zeroMatrixInplace([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))
print(zeroMatrixOptimal([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))
