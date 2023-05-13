n, m = map(int, input().split())
matrix = [0 for j in range(m + 1)]
matrix[0] = 1
k = list(map(int, input().split()))
for j in range(n):
    w = k[j]
    if j == 0:
        if w <= m:
            matrix[w] = 1
    else:
        if w <= m:
            for i in range(m, -1, -1):
                if matrix[i] == 1:
                    if i + w <= m:
                        matrix[i + w] = 1
            matrix[w] = 1
for j in range(m, -1, -1):
    if matrix[j] == 1:
        print(j)
        break