n = int(input())
max_counter = n - 1
my_list = list(map(int, input().split()))
if my_list:
    max_variable = my_list[-1]
for j in range(n):
    if my_list[j] > max_variable:
        max_counter = j
        max_variable = my_list[j]
if my_list:
    my_list[-1], my_list[max_counter] = max_variable, my_list[-1]
print(*my_list)
