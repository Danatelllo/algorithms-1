def bin_search_min(end, start, arr, elem):
    mid = (end + start) // 2
    while start + 1 < end:
        if arr[mid] > elem:
            end = mid
        if arr[mid] < elem:
            start = mid
        if arr[mid] == elem:
            end = mid
        mid = (end + start) // 2
    if arr[start] == elem:
        return start
    if arr[end] == elem:
        return end
    return -1


def bin_search_max(end, start, arr, elem):
    mid = (end + start) // 2
    while start + 1 < end:
        if arr[mid] > elem:
            end = mid
        if arr[mid] < elem:
            start = mid
        if arr[mid] == elem:
            start = mid
        mid = (end + start) // 2
    if arr[end] == elem:
        return end
    if arr[start] == elem:
        return start
    return -1


n = int(input())
my_list = list(map(int, input().split()))
k = int(input())
commands = list(map(int, input().split()))
for x in commands:
    answer1 = bin_search_min(n - 1, 0, my_list, x)
    answer2 = bin_search_max(n - 1, 0, my_list, x)
    if answer1 == answer2 == -1:
        print(0, 0)
    else:
        print(answer1 + 1, answer2 + 1)