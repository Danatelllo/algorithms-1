n, k = map(int, input().split())
a = [0 for j in range(31)]
a[1] = 1
a[2] = 1
ans = 0
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    for j in range(3, n + 1):
        for i in range(max(j - k, 1), j):
            a[j] += a[i]
    print(a[n])