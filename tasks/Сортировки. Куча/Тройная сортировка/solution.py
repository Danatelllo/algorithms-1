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


len1, len2, len3 = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = list(map(int, input().split()))
result1 = merge(len1, len2, list1, list2, [])
print(*merge(len(result1), len3, result1, list3, []))