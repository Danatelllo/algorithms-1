def merge(m, n, l, r, result):
    k, j = 0, 0
    counter = 0
    while counter < m + n - 1:
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
len2 = int(input())
list2 = list(map(int, input().split()))
if not list1 and list2:
    print(*list2)
elif not list2 and list1:
    print(*list1)
elif list1 and list2:
    print(*merge(len1, len2, list1, list2, []))