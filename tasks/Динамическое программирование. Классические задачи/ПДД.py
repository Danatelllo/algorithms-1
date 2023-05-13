n, m = map(int, input().split())
a = []
for j in range(n):
    a.append(list(map(int, input().split())))
    if j == 0:
        for i in range(1, m):
            a[0][i] += a[0][i - 1]
    if j > 0:
        a[j][0] += a[j - 1][0]
i = 0
j = 0
for i in range(1, n):
    for j in range(1, m):
        a[i][j] += min(a[i - 1][j], a[i][j - 1])
i, j = n - 1, m - 1
s = '\n' + str(i + 1) + ' ' + str(j + 1)
counter = 0
while i + j != 0:
    if i > 0 and j > 0 and a[i - 1][j] < a[i][j - 1]:
        s = '\n' + str(i) + ' ' + str(j + 1) + s
        i -= 1
    elif i > 0 and j > 0:
        s = '\n' + str(i + 1) + ' ' + str(j) + s
        j -= 1
    elif i == 0:
        s = '\n' + str(i + 1) + ' ' + str(j) + s
        j -= 1
    else:
        s = '\n' + str(i) + ' ' + str(j + 1) + s
        i -= 1
    counter += 1
print(a[n - 1][m - 1])
print(counter + 1)
print(s[1:])