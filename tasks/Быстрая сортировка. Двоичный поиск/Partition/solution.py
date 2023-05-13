def partition(n, a, x):
    start = 0
    end = n - 1
    counter1 = 0
    counter2 = 0
    while start < end:
        while start <= n - 1 and a[start] < x:
            start += 1
        while a[end] >= x and end >= 0:
            end -= 1
        if end <= start:
            break
        if start < end:
            a[start], a[end] = a[end], a[start]
    for j in range(n):
        if a[j] < x:
            counter1 += 1

        if a[j] >= x:
            counter2 += n - j
            break
    return counter2, counter1


len_a = int(input())
if len_a:
    arr = list(map(int, input().split()))
    position = int(input())
    answer = partition(len_a, arr, position)
    print(answer[1])
    print(answer[0])
else:
    print(0)
    print(0)