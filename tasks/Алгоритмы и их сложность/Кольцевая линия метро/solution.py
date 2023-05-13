a, b, c = map(int, input().split())
if abs(b - c) == 1:
    print(0)
elif b < c:
    print(min(c - b - 1, abs(1 - b) + a - c))
else:
    b, c = c, b
    print(min(c - b - 1, abs(1 - b) + a - c))
