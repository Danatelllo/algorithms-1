import collections
my_deque = collections.deque()
with open('input.txt', 'r', encoding='utf8') as f:
    for row in f:
        values = row.split()
        if values[0] == 'push_front':
            my_deque.appendleft(values[1])
            print('ok')
        if values[0] == 'push_back':
            my_deque.append(values[1])
            print('ok')
        if values[0] == 'pop_front' and not my_deque:
            print('error')
        if values[0] == 'pop_front' and my_deque:
            print(my_deque.popleft())
        if values[0] == 'pop_back' and not my_deque:
            print('error')
        if values[0] == 'pop_back' and my_deque:
            print(my_deque.pop())
        if values[0] == 'front' and my_deque:
            print(my_deque[0])
        if values[0] == 'front' and not my_deque:
            print('error')
        if values[0] == 'back' and my_deque:
            print(my_deque[-1])
        if values[0] == 'back' and not my_deque:
            print('error')
        if values[0] == 'size':
            print(len(my_deque))
        if values[0] == 'clear':
            print('ok')
            my_deque.clear()
        if values[0] == 'exit':
            print('bye')
            break
