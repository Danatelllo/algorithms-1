k = int(input())
ss = input()
ss += ss[::-1]
z = [0 for j in range(len(ss))]
i = 1
start, end = 0, 0
for i in range(1, len(ss)):
    if i <= end:
        z[i] = min(z[i - start], end - i + 1)
    while i + z[i] < len(ss) and ss[z[i]] == ss[i + z[i]]:
        z[i] += 1
    if i + z[i] - 1 > end:
        start = i
        end = i + z[i] - 1
print(*reversed(z[k:]))