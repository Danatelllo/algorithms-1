import collections
n = int(input())
a = list(map(int, input().split()))
ans = [1 for j in range(n)]
maxim = 0
for j in range(1, n):
    for i in range(j):
        if a[j] > a[i]:
            if ans[i] + 1 > ans[j]:
                ans[j] = ans[i] + 1
                if ans[j] > maxim:
                    maxim = ans[j]
s = collections.deque()
for j in range(n - 1, -1, -1):
    if ans[j] == maxim:
        s.appendleft(a[j])
        maxim -= 1
print(*s)
