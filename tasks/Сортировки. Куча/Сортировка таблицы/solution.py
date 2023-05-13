from collections import deque
n = int(input())
order = list(map(int, input().split()))
my_dict = {}
for j in range(n - 1, -1, -1):
    if order[j] not in my_dict:
        my_dict[order[j]] = 1
print(len(my_dict))
print(*reversed(my_dict.keys()))