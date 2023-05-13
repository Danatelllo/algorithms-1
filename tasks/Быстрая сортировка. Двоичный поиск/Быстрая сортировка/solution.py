import random


def quicksort(my_list, start, end):
    if start >= end:
        return my_list
    else:
        pivot = random.choice(my_list[start:end])
        i = start
        j = end
        while i <= j:
            while my_list[i] < pivot:
                i += 1
            while my_list[j] > pivot:
                j -= 1
            if i <= j:
                my_list[i], my_list[j] = my_list[j], my_list[i]
                i += 1
                j -= 1
        quicksort(my_list, start, j)
        quicksort(my_list, i, end)


n = int(input())
arr = list(map(int, input().split()))
quicksort(arr, 0, n - 1)
print(*arr)