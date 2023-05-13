n, m = map(int, input().split())
matrix = [0 for j in range(m + 1)]
k = list(map(int, input().split()))
c = list(map(int, input().split()))
for j in range(n):
    w = k[j]
    if j == 0:
        if w <= m:
            matrix[w] = c[j]
    else:
        if w <= m:
            for i in range(m, -1, -1):
                if matrix[i] != 0:
                    if i + w <= m and matrix[i + w] < c[j] + matrix[i]:
                        matrix[i + w] = c[j] + matrix[i]
            if matrix[w] < c[j]:
                matrix[w] = c[j]
print(max(matrix))
