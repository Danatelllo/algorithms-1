n, m = map(int, input().split())
s = []
for j in range(n):
    x, y = map(int, input().split())
    s.append([min(x, y), -1])
    s.append([max(y, x), 1])
b = list(map(int, input().split()))
for j in range(m):
    b[j] = [b[j], 0, j]
s += b
s.sort()
counter = 0
for i in range(2 * n + m):
    if s[i][1] == -1:
        counter += 1
    if s[i][1] == 0:
        b[s[i][2]] = counter
    if s[i][1] == 1:
        counter -= 1
print(*b)