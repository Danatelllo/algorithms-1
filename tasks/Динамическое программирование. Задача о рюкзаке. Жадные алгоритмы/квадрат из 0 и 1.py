n, k, s = map(int, input().split())
matrix = [[0 for j in range(n)] for i in range(n)]
m = n // k
for l in range(m):
    for j in range(m):
        p = s
        for e in range(l * k, k + k * l):
            for i in range(j * k, k + k * j):
                if p > 0:
                    matrix[e][i] = 1
                    p -= 1
                else:
                    break
if n % k == 0:
    for j in range(n):
        print(*matrix[j])
else:
    p = -1
    for i in range(n // k * k, n):
        p += 1
        for j in range(n):
            matrix[j][n // k * k + p] = matrix[j][p]
    p = -1
    for i in range(n // k * k, n):
        p += 1
        matrix[i] = matrix[p]
    for j in range(n):
        print(*matrix[j])