n = int(input())
k1 = 1
k2 = 1
ans = 4
if n == 1:
    print(2)
elif n == 2:
    print(4)
else:
    for j in range(3, n + 1):
        t = ans - k2 + ans
        b = ans - k1 - k2
        k2 = k1
        k1 = b
        ans = t
    print(ans)