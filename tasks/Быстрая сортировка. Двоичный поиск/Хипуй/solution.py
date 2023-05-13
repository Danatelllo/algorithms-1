heap = ['Hello']
n = int(input())
for j in range(n):
    commands = list(map(int, input().split()))
    if commands[0] == 0:
        if len(heap) == 1:
            heap.append(commands[1])
        else:
            heap.append(commands[1])
            value = len(heap) - 1
            while value // 2 >= 1 and \
                    heap[value] > heap[value // 2]:
                heap[value // 2], heap[value] = \
                    heap[value], heap[value // 2]
                value //= 2

    else:
        if len(heap) == 2:
            print(heap[1])
            heap.pop()
        else:
            print(heap[1])
            heap[1] = heap[-1]
            heap.pop()
            value = 1
            length = len(heap) - 1
            while length >= value * 2 + 1 and heap[value] < \
                    max(heap[value * 2], heap[value * 2 + 1]):
                if heap[value * 2] > heap[value * 2 + 1]:
                    heap[value * 2], heap[value] = \
                        heap[value], heap[value * 2]
                    value = value * 2
                else:
                    heap[value * 2 + 1], heap[value] = \
                        heap[value], heap[value * 2 + 1]
                    value = value * 2 + 1
            if length == value * 2 and heap[value] < \
                    heap[value * 2]:
                heap[value], heap[value * 2] = heap[value * 2], heap[value]