number1 = [[0] for j in range(10)]
number2 = [[0] for i in range(10)]
s = input()
for x in s:
    number1[9 - int(x)][0] += 1
s = input()
for x in s:
    number2[9 - int(x)][0] += 1
max_number = ''
for j in range(9, -1, -1):
    k = min(number1[9 - j][0], number2[(9 - j)][0])
    if k > 0 and j != 0:
        max_number += (str(j) * k)
    elif j == 0 and max_number:
        max_number += (str(j) * k)
    if j == 0 and max_number == '' and k > 0:
        max_number = '0'

if max_number or max_number == '0':
    print(max_number)
else:
    print(-1)