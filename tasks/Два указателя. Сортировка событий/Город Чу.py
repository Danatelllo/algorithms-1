n, m = map(int, input().split())
l = 0
r = 1
answer = 0
mon = list(map(int, input().split()))
while mon[-1] - mon[l] > m and l < n:
    if mon[r] - mon[l] > m:
        answer += n - r
        l += 1
    else:
        r += 1
print(answer)
