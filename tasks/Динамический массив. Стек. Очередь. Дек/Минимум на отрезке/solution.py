import collections
my_deque = collections.deque()
n, k = map(int, input().split())
my_list = list(map(int, input().split()))
flag = 1
my_deque.append(my_list[0])
for j in range(1, n):
    if k == 0:
        break
    elif k == 1:
        if flag:
            print(my_deque[0])
            flag -= 1
        print(my_list[j])
    elif k > 1:
        if my_list[j] < my_deque[0]:
            my_deque.clear()
            my_deque.append(my_list[j])
        elif my_list[j] > my_deque[-1]:
            my_deque.append(my_list[j])
        else:
            while my_list[j] < my_deque[-1] and my_deque:
                my_deque.pop()
            my_deque.append(my_list[j])
        if j + 1 >= k:
            if my_list[j + 1 - k] == my_deque[0]:
                print(my_deque.popleft())
                flag = True
            else:
                print(my_deque[0])
