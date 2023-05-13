n = int(input())
k = 0
maxim = 0
flag = False
minim = -float('inf')
arr = list(map(int, input().split()))
for j in range(n):
    if k + arr[j] >= 0:
        k += arr[j]
        flag = True
        if k > maxim:
            maxim = k
    else:
        k = 0
        if arr[j] > minim and arr[j] != 0:
            minim = arr[j]

if k == 0 and not flag:
    print(minim)
else:
    print(maxim)