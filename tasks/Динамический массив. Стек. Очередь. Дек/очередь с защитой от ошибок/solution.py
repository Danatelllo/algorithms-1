import collections
q = collections.deque()
with open('input.txt', 'r', encoding='utf8') as f:
    for raw in f:
        values = raw.split()
        if values[0] == 'push':
            q.append(values[1])
            print('ok')
        if values[0] == 'pop':
            if q:
                print(q[0])
                q.popleft()
            else:
                print('error')
        if values[0] == 'front':
            if q:
                print(q[0])
            else:
                print('error')
        if values[0] == 'size':
            print(len(q))
        if values[0] == 'clear':
            q.clear()
            print('ok')
        if values[0] == 'exit':
            print('bye')
            break
