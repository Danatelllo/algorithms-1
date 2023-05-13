n, m = map(int, input().split())
matrix = [[0 for j in range(m + 2)] for i in range(m + 2)]
points = list(map(int, input().split()))
points = [0] + points + [n]
for j in range(2, m + 2):
    for i in range(m - j + 2):
        c = min(matrix[x][i] + matrix[j + i][x] for x in range(i + 1, j + i))
        matrix[j + i][i] = points[j + i] - points[i] + c
print(matrix[m + 1][0])