keyboard = dict()
n = int(input())
m = list(map(int, input().split()))
for j in range(n):
    keyboard[j + 1] = m[j]
n = int(input())
m = list(map(int, input().split()))
for i in range(n):
    keyboard[m[i]] -= 1
for j in keyboard.values():
    if j < 0:
        print('yes')
    else:
        print('no')
