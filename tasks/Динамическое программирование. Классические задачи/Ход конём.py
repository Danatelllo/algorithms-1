n, m = map(int, input().split())
ans = [[0 for i in range(m)] for j in range(n)]
ans[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        if i - 2 >= 0 and j - 1 >= 0:
            ans[i][j] += ans[i - 2][j - 1]
        if i - 1 >= 0 and j - 2 >= 0:
            ans[i][j] += ans[i - 1][j - 2]
print(ans[n - 1][m - 1])
