stack = []
with open('input.txt', 'r', encoding='utf8') as f:
    for row in f:
        values = row.split()
        if values[0] == 'push':
            print('ok')
            stack.append(values[1])
        if values[0] == 'pop':
            print(stack[-1])
            stack.pop(len(stack) - 1)
        if values[0] == 'back':
            print(stack[-1])
        if values[0] == 'size':
            print(len(stack))
        if values[0] == 'clear':
            stack.clear()
            print('ok')
        if values[0] == 'exit':
            print('bye')
            break