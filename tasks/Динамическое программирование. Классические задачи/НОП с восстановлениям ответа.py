import collections


s = collections.deque()
n = int(input())
s1 = input().split()
m = int(input())
s2 = input().split()
answer = [[0 for i in range(m + 1)] for j in range(n + 1)]
for j in range(n):
    for i in range(m):
        if s1[j] != s2[i]:
            answer[j + 1][i + 1] = max(answer[j][i + 1], answer[j + 1][i])
        else:
            answer[j + 1][i + 1] = answer[j][i] + 1
j, i = n, m
while answer[j][i]:
    if answer[j][i] == answer[j][i - 1]:
        i -= 1
    elif answer[j][i] == answer[j - 1][i]:
        j -= 1
    else:
        s.appendleft(s2[i - 1])
        j -= 1
        i -= 1
print(*s)