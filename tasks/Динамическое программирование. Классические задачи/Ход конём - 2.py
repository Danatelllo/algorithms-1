n, m = map(int, input().split())
ans = [[0 for i in range(m)] for j in range(n)]
ans[0][0] = 1
x = 0
y = 0
t = 0
flag = True
if n == 1 or m == 1:
    print(0)
else:
    while True:
        a, b = x, y
        while m - 1 >= x >= 0 and 0 <= y <= n - 1:
            if y - 2 >= 0 and x - 1 >= 0:
                t += ans[y - 2][x - 1]
            if y - 2 >= 0 and x + 1 <= m - 1:
                t += ans[y - 2][x + 1]
            if x - 2 >= 0 and y + 1 <= n - 1:
                t += ans[y + 1][x - 2]
            if x - 2 >= 0 and y - 1 >= 0:
                t += ans[y - 1][x - 2]
            ans[y][x] += t
            t = 0
            y += 1
            x -= 1
        if not flag:
            x = m - 1
            y = b + 1
            if y == n:
                break
        if flag:
            if x < m - 1:
                x = a + 1
                y = 0
            else:
                flag = False
                x = m - 1
                y = 1
    print(ans[n - 1][m - 1])