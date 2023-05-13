import string


def bin_p(d, start, end, start2):
    mid = (start + end) // 2
    while start < end - 1:
        a = f(d, start, start2, mid - start + 1)
        if not a:
            start2 += mid - start
            start = mid
        elif a:
            end = mid
        mid = (start + end) // 2
    return start, end


def f(d, F1, F2, l):
    if F2 > 0:
        a = (h[F1 + l - 1] + h[F2 - 1] * d[l]) % p
    else:
        a = h[F1 + l - 1] % p
    if F1 > 0:
        b = (h[F2 + l - 1] + h[F1 - 1] * d[l]) % p
    else:
        b = h[F2 + l - 1] % p
    if a == b:
        return 0
    else:
        return True


s = string.ascii_letters
dc = {}
k = 1
for i in s:
    dc[i] = k
    k += 1
deg = []
ss = input()
k = int(input())
if len(ss) > 0:
    h = [dc[ss[0]]]
    deg = [1]
    x = 53
    p = 2728960988081814927215584400906674790392693735419556071132025339
    n = len(ss)
    for j in range(1, len(ss)):
        h.append((h[-1] * x + dc[ss[j]]) % p)
        deg.append((deg[-1] * x) % p)
    ans = 0
    for i in range(k):
        l, a, b = map(int, input().split())
        if not (f(deg, a, b, l)):
            print(0)
        else:
            q, y = bin_p(deg, a, l - 1 + a, b)
            if ss[q] == ss[b + q - a]:
                if ss[y] > ss[b + y - a]:
                    print(1)
                else:
                    print(-1)
            else:
                if ss[q] > ss[b + q - a]:
                    print(1)
                else:
                    print(-1)