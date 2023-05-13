def merge(n, my_list, result):
    a = my_list[:n // 2]
    b = my_list[n // 2:]
    if n == 1:
        return my_list
    l = merge(len(a), a, [])
    r = merge(len(b), b, [])
    k, j = 0, 0
    counter = 0
    while counter < len(l) + len(r) - 1:
        counter += 1
        if l[k] <= r[j]:
            result.append(l[k])
            k += 1
            if k == len(l):
                result += r[j:]
                break
        elif r[j] < l[k]:
            result.append(r[j])
            j += 1
            if j == len(r):
                result += l[k:]
                break
    return result


len1 = int(input())
list1 = list(map(int, input().split()))
if len1:
    print(*merge(len1, list1, []))