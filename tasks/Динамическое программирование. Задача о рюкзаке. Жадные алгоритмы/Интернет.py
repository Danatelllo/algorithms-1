m = int(input())
s = list(map(int, input().split()))
i = 0
for k in range(31):
    s[k] = [s[k], 2 ** i]
    i += 1
i = 0
while i < 30:
    if 2 * s[i][0] > s[i + 1][0]:
        s[i + 1][0] = 2 * s[i][0]
    i += 1
minim = 0
answer = set()
ans = 0
for j in range(30, -1, -1):
    if m - s[j][0] <= 0 and not answer:
        answer.add(s[j][1])
    if m - s[j][0] >= 0:
        m -= s[j][0]
        ans += s[j][1]
        if m == 0:
            answer.add(ans)
    if m - s[j][0] < 0 and answer:
        answer.add(ans + s[j][1])
print(min(answer))