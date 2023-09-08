# 01 02 03 04
# 05 06 07 08
# 09 10 11 12
# 13 14 15 16

# =>
# 13 09 05 01
# 14 10 06 02
# 15 11 07 03
# 16 12 08 04

"""
[0, 0] -> [0, 3]
[0, 1] -> [1, 3]
[0, 2] -> [2, 3]
[0, 3] -> [3, 3]
[1, 0] -> [0, 2]
[1, 1] -> [1, 2]
[1, 2] -> [2, 2]
[3, 1] -> [1, 1]

[i, j] -> [j, n - i - 1]
[j, n - i - 1] -> [n - i - 1, n - j - 1]
[n - i - 1, n - j - 1] -> [n - j - 1, i]
[n - j - 1, i] -> [i, j]

13 02 03 01
05 06 07 08
09 10 11 12
16 14 15 04
->
13 09 03 01
05 06 07 02
15 10 11 12
16 14 08 04
->
13 09 05 01
14 06 07 02
15 10 11 03
16 12 08 04
"""


# Time complexity: O(n^2)
# Space complexity: O(n^2)
def rotateMatrix90DegreeBruteForce(matrix):
    N = len(matrix)
    tmpMatrix = [[None for i in range(N)]
                 for j in range(N)]

    # Values to fill in order
    values = []
    for i in range(N):
        for j in range(N):
            values.append(matrix[i][j])

    # Fill new matrix
    k = 0
    for j in range(N - 1, -1, -1):
        for i in range(N):
            tmpMatrix[i][j] = values[k]
            k += 1

    return tmpMatrix

# Brute force: O(n^2)
# BCR: O(n^2)
# Can reduce space to O(1) only -> In place rotation


# Time complexity: O(n^2)
# Space complexity: O(1)
def rotateMatrix90DegreeInplace(matrix):
    N = len(matrix)

    for i in range(N // 2):
        for j in range(i, N - i - 1):
            # Store all replace values
            # values = [matrix[i][j], matrix[j][N - i - 1],
            #           matrix[N - i - 1][N - j - 1], matrix[N - j - 1][i]]
            # matrix[j][N - i - 1] = values[0]
            # matrix[N - i - 1][N - j - 1] = values[1]
            # matrix[N - j - 1][i] = values[2]
            # matrix[i][j] = values[3]

            # Store only the first item
            top = matrix[i][j]
            matrix[i][j] = matrix[N - j - 1][i]
            matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1]
            matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1]
            matrix[j][N - i - 1] = top

    return matrix


print(rotateMatrix90DegreeBruteForce(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
)
print(rotateMatrix90DegreeInplace(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
)

print(rotateMatrix90DegreeBruteForce(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
)
print(rotateMatrix90DegreeInplace(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
)
