n = int(input())
m = n
time = []
for j in range(n):
    a, b, c, d = map(int, input().split())
    if a == c and b == d:
        m -= 1
    else:
        start_time = a * 60 + b
        end_time = c * 60 + d
        time.append((start_time, -1, j))
        time.append((end_time, 1, j))
time.sort()
start = 0
ans = 0
answer = []
openly = set()
k = 0
if m > 1:
    for j in range(2 * m):
        if time[j][1] == -1:
            start = time[j][0]
            openly.add(time[j][2])
        if time[j][1] == 1:
            if time[j][2] in openly:
                openly.remove(time[j][2])
    for j in range(2 * m):
        if time[j][1] == -1:
            start = time[j][0]
            openly.add(time[j][2])
        if time[j][1] == 1:
            if len(openly) == m:
                if start > time[j][0]:
                    ans += (1440 - abs(- start + time[j][0]))
                else:
                    ans += time[j][0] - start
            openly.remove(time[j][2])
    print(ans)
else:
    if m == 1:
        if time[0][1] == -1:
            ans += time[1][0] - time[0][0]
        else:
            ans += (1440 - abs(time[1][0] - time[0][0]))
        print(ans)
    else:
        print(24 * 60)