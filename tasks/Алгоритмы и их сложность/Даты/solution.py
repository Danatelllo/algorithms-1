a, b, c = map(int, input().split())
if a <= 12 and b <= 12 and b != a:
    print(0)
elif a == b <= 12:
    print(1)
elif a > 12 and b <= 12:
    print(1)
elif a <= 12 and b > 12:
    print(1)
else:
    print(0)