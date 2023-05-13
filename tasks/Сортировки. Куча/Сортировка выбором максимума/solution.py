def f(m, my_list):
    for j in range(m):
        min_variable = float('inf')
        index_min_variable = 0
        for i in range(j, m):
            if my_list[i] < min_variable:
                min_variable = my_list[i]
                index_min_variable = i
        my_list[index_min_variable] = my_list[j]
        my_list[j] = min_variable
        print(my_list[j], end=' ')


n = int(input())
if n:
    arr = list(map(int, input().split()))
    f(n, arr)
