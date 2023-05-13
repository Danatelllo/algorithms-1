n, m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
Y_new = []
X_new = []
i = 0
for x in X:
    X_new.append([x, i])
    i += 1
i = 0
for y in Y:
    Y_new.append([y, i])
    i += 1
ans = dict()
X_new.sort()
Y_new.sort()
i = 1
for j in range(m):
    if X_new[i - 1][0] + 1 <= Y_new[j][0]:
        ans[(X_new[i - 1][0], X_new[i - 1][1])] = Y_new[j][1] + 1
        i += 1
print(len(ans))
for j in range(n):
    if (X[j], j) not in ans:
        print(0, end=' ')
    else:
        print(ans[(X[j], j)], end=' ')