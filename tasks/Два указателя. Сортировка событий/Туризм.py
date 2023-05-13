n = int(input())
length = []
x1, y1 = map(int, input().split())
length.append((0, 0))
for j in range(1, n):
    x2, y2 = map(int, input().split())
    if y2 - y1 > 0:
        length.append((y2 - y1 + length[j - 1][0], length[j - 1][1]))
    else:
        length.append((length[j - 1][0], y1 - y2 + length[j - 1][1]))
    y1 = y2
M = int(input())
for j in range(M):
    start, end = map(int, input().split())
    if start < end:
        print(length[end - 1][0] - length[start - 1][0])
    else:
        print((length[start - 1][1] - length[end - 1][1]))