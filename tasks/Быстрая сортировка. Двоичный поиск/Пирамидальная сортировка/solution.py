def sift_down(heap, length):
    for j in range((length + 1) // 2 - 1, -1, -1):
        value = j
        while length >= value * 2 + 2 and heap[value] < \
                max(heap[value * 2 + 1], heap[value * 2 + 2]):
            if heap[value * 2 + 2] > heap[value * 2 + 1]:
                heap[value], heap[value * 2 + 2] = \
                    heap[value * 2 + 2], heap[value]
                value *= 2
                value += 2
            else:
                heap[value], heap[value * 2 + 1] = \
                    heap[value * 2 + 1], heap[value]
                value *= 2
                value += 1
        if length >= value * 2 + 1 and heap[value] < \
                heap[value * 2 + 1]:
            heap[value], heap[value * 2 + 1] = \
                heap[value * 2 + 1], heap[value]


def heap_sort(heap, n):
    for j in range(1, n + 1):
        heap[n + 1 - j], heap[0] = heap[0], heap[n + 1 - j]
        length = n - j
        value = 0
        while length >= value * 2 + 2 and heap[value] < \
                max(heap[value * 2 + 1], heap[value * 2 + 2]):
            if heap[value * 2 + 2] > heap[value * 2 + 1]:
                heap[value], heap[value * 2 + 2] = \
                    heap[value * 2 + 2], heap[value]
                value *= 2
                value += 2
            else:
                heap[value], heap[value * 2 + 1] = \
                    heap[value * 2 + 1], heap[value]
                value *= 2
                value += 1
        if length >= value * 2 + 1 and heap[value] < \
                heap[value * 2 + 1]:
            heap[value], heap[value * 2 + 1] = \
                heap[value * 2 + 1], heap[value]


k = int(input())
my_heap = list(map(int, input().split()))
sift_down(my_heap, k - 1)
heap_sort(my_heap, k - 1)
print(*my_heap)
