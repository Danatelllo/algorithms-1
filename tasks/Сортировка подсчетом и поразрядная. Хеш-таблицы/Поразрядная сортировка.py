n = int(input())
a = [input() for j in range(n)]
buckets = [[] for i in range(10)]
print('Initial array:')
print(*a, sep=', ')
k = 1
p = 1
for i in range(len((a[0])) - 1, -1, -1):
    k *= 10
    for j in range(n):
        digit = int(a[j][i]) % k
        buckets[digit].append(a[j])
    print('**********')
    print('Phase', p)
    if not buckets[0]:
        print('Bucket 0: empty')
    else:
        print('Bucket 0:', ', '.join(buckets[0]))
    if not buckets[1]:
        print('Bucket 1: empty')
    else:
        print('Bucket 1:', ', '.join(buckets[1]))
    if not buckets[2]:
        print('Bucket 2: empty')
    else:
        print('Bucket 2:', ', '.join(buckets[2]))
    if not buckets[3]:
        print('Bucket 3: empty')
    else:
        print('Bucket 3:', ', '.join(buckets[3]))
    if not buckets[4]:
        print('Bucket 4: empty')
    else:
        print('Bucket 4:', ', '.join(buckets[4]))
    if not buckets[5]:
        print('Bucket 5: empty')
    else:
        print('Bucket 5:', ', '.join(buckets[5]))
    if not buckets[6]:
        print('Bucket 6: empty')
    else:
        print('Bucket 6:', ', '.join(buckets[6]))
    if not buckets[7]:
        print('Bucket 7: empty')
    else:
        print('Bucket 7:', ', '.join(buckets[7]))
    if not buckets[8]:
        print('Bucket 8: empty')
    else:
        print('Bucket 8:', ', '.join(buckets[8]))
    if not buckets[9]:
        print('Bucket 9: empty')
    else:
        print('Bucket 9:', ', '.join(buckets[9]))
    a = []
    for j in range(10):
        a += buckets[j]
    buckets = [[] for i in range(10)]
    p += 1
print('**********')
print('Sorted array:')
print(*a, sep=', ')
