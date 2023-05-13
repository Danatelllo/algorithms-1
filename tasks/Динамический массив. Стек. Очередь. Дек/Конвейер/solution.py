n = int(input())
cont_gone = float('inf')
my_stack = []
flag = True
for j in range(n):
    row = list(map(float, input().split()))
    for i in range(1, int(row[0]) + 1):
        if i == 1:
            my_stack.append(row[i])
        elif row[i] <= my_stack[-1]:
            if row[i] > cont_gone or cont_gone == float('inf'):
                my_stack.append(row[i])
            else:
                flag = False
                break
        elif row[i] > my_stack[-1]:
            while my_stack and row[i] > my_stack[-1]:
                if my_stack[-1] < cont_gone:
                    cont_gone = my_stack[-1]
                my_stack.pop(-1)
            my_stack.append(row[i])
    print(int(flag))
    my_stack.clear()
    flag = True
    cont_gone = float('inf')