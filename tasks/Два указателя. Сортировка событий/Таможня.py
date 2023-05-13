n = int(input())
s = []
counter = 0
for j in range(n):
    a, b = map(int, input().split())
    s.append([a, 1])
    s.append([a + b, -1])
answer = -float('inf')
counter = 0
s.sort()
for i in range(2 * n):
    if s[i][1] == 1:
        counter += 1
        if counter > answer:
            answer = counter
    if s[i][1] == -1:
        counter -= 1
print(answer)
