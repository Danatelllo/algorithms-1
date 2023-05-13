import collections
n, m = map(int, input().split())
arr = [[0] * (m + 1)]
w = list(map(int, input().split()))
c = list(map(int, input().split()))
maxim = 0
end = 0
for j in range(n):
    if j == 0:
        if w[j] <= m:
            arr[0][w[j]] = c[j]
            maxim = c[j]
            end = w[j]
    else:
        arr_cop = arr[-1].copy()
        if w[j] <= m:
            for i in range(m - w[j], -1, -1):
                if arr_cop[i] or i == 0:
                    if arr_cop[i] + c[j] > arr_cop[i + w[j]]:
                        arr_cop[i + w[j]] = arr_cop[i] + c[j]
                        if arr_cop[i + w[j]] > maxim:
                            maxim = arr_cop[i + w[j]]
                            end = i + w[j]
        arr.append(arr_cop)
'''Восстановление ответа вошло в чат'''
if maxim:
    j = n - 1
    d = collections.deque()
    while maxim >= 0 and j >= 0:
        if end - w[j] >= 0 and maxim - c[j] == arr[j - 1][end - w[j]]:
            maxim = arr[j - 1][end - w[j]]
            end -= w[j]
            d.appendleft(j + 1)
        j -= 1
    for j in range(len(d)):
        print(d[j])