n = int(input())
counter = 0
my_list = list(map(int, input().split()))
for j in range(n):
    for i in range(n - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i + 1], my_list[i] = my_list[i], my_list[i + 1]
            counter += 1
print(counter)
