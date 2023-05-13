n, m = map(int, input().split())
ans = n
s = set()
for j in range(m):
    s.add(tuple(map(int, input().split())))
ans = n
k = -1
for x in sorted(s):
    if k == -1:
        k = x[1]
        ans -= x[1] - x[0] + 1
    elif x[0] <= k <= x[1]:
        ans -= x[1] - k
        k = x[1]
    elif k < x[0]:
        k = x[1]
        ans -= x[1] - x[0] + 1
print(ans)