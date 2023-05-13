n = int(input())
my_list = list(map(int, input().split()))
for j in range(1, n):
    k = j
    subject = my_list[j]
    while k > 0 and subject < my_list[k - 1]:
        my_list[k] = my_list[k - 1]
        k -= 1
    if k < j:
        my_list[k] = subject
        print(*my_list)