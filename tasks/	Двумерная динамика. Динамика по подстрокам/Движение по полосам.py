m, n = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n - 1)]
matrix.append([1 for x in range(m)])
for j in range(n - 2, -1, -1):
    for i in range(m):
        if j == 0:
            matrix[j][i] += matrix[j][i - 1]
        if j == n - 2:
            matrix[j][i] += matrix[j + 1][i]
            if i + 1 < m:
                matrix[j][i] += matrix[j + 1][i + 1]
        else:
            matrix[j][i] += matrix[j + 1][i]
            if i + 1 < m:
                matrix[j][i] += 2 * sum(matrix[j + 1][i + 1:])
print(matrix[0][m - 1])