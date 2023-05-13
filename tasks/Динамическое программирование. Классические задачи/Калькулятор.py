import collections
n = int(input())
a = [0 for j in range(n + 1)]
a[1] = 0
if n == 2:
    print(1)
    print(1, 2)
elif n == 3:
    print(1)
    print(1, 3)
elif n == 1:
    print(0)
    print(1)
else:
    a[2] = 1
    a[3] = 1
    ans = []
    for j in range(4, n + 1):
        if j % 2 == 0 and j % 3 == 0:
            a[j] += 1 + min(a[j // 2], a[j // 3], a[j - 1])
        elif j % 2 == 0:
            a[j] += 1 + min(a[j // 2], a[j - 1])
        elif j % 3 == 0:
            a[j] += 1 + min(a[j // 3], a[j - 1])
        else:
            a[j] += 1 + a[j - 1]
    s = str(n)
    k = n
    print(a[n])
    s = collections.deque()
    s.append(n)
    p = a[n]
    while k != 1:
        if k % 3 == 0 and p - 1 == a[k // 3]:
            s.appendleft(k // 3)
            k //= 3
            p -= 1
        elif k % 2 == 0 and p - 1 == a[k // 2]:
            s.appendleft(k // 2)
            k //= 2
            p -= 1
        else:
            s.appendleft(k - 1)
            k -= 1
            p -= 1
    for j in range(len(s)):
        print(s[j], end=' ')