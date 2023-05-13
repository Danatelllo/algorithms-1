n, k = map(int, input().split())
s = input()
d = dict()
i = 0
j = 0
maxim = 0
flag = True
begin = 0
p = 0
if n == 1:
    print(1, 1)
else:
    while i < n - 1 and j <= n - 1:
        if s[j] not in d:
            d[s[j]] = 1
        else:
            if j > p:
                d[s[j]] += 1
                p = j
        if d[s[j]] > k:
            if j - i > maxim:
                maxim = j - i
                begin = i
            d[s[i]] -= 1
            i += 1
        elif d[s[j]] <= k and j == n - 1:
            if j - i + 1 > maxim:
                maxim = j - i + 1
                begin = i
            break
        else:
            j += 1
    print(maxim, begin + 1)
