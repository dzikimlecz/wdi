def determinant(matrix):
    N = len(matrix)
    if N == 1:
        return matrix[0][0]
    det = 0
    for i in range(N):
        newMatrix = [[0 for _ in range(N - 1)] for _ in range(N - 1)]
        for row in range(i):
            for col in range(N - 1):
                newMatrix[row][col] = matrix[row][col + 1]
        for row in range(i + 1, N):
            for col in range(N - 1):
                newMatrix[row - 1][col] = matrix[row][col + 1]
        if i % 2 == 0:
            det += matrix[i][0] * determinant(newMatrix)
        else:
            det -= matrix[i][0] * determinant(newMatrix)
    return det


if __name__ == '__main__':
    m = [
        [1, 6, 6],
        [6, 2, 6],
        [6, 6, 3]
    ]
    print(determinant(m))