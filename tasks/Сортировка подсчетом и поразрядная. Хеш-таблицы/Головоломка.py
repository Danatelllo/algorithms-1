import collections
n, m = map(int, input().split())
d = collections.defaultdict(int)
for j in range(n):
    s = input()
    for i in range(n):
        d[s[i]] += 1
for i in range(m):
    s = input()
    for j in range(len(s)):
        d[s[j]] -= 1
answer = ''
for i in d:
    if d[i] > 0:
        answer += d[i] * i
print(answer)