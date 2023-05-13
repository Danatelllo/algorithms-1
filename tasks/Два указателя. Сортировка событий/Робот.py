ans = 0
k = int(input())
s = input()
n = len(s)
p = 0
r = 0
time_ans = 0
j = 0
flag = True
while j < n - k:
    if time_ans == 0:
        p = j
        r = j + k
    else:
        j = p + 1
        r = j + k
        p = j
        if time_ans > 1:
            ans += time_ans * (time_ans + 1) // 2
        else:
            ans += 1
        time_ans = 0
    while r < n and s[p] == s[r]:
        time_ans += 1
        r += 1
        p += 1
    j += 1
    if j >= n - k:
        ans += time_ans * (time_ans + 1) // 2
print(ans)