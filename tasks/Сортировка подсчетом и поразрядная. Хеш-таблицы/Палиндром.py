expression = ''
words = dict()
n = int(input())
row = input()
for x in row:
    if x not in words:
        words[x] = 1
    else:
        words[x] += 1
words = list(map(list, sorted(words.items())))
flag = False
mid = ''
for j in range(len(words)):
    if words[j][1] % 2 == 0:
        expression += words[j][0] * (words[j][1] // 2)
    elif words[j][1] % 2 == 1:
        if words[j][1] // 2 > 0:
            if not flag:
                mid = words[j][0]
                flag = True
            words[j][1] -= 1
            expression += words[j][0] * (words[j][1] // 2)
        elif words[j][1] // 2 == 0:
            if not flag:
                mid = words[j][0]
                flag = True

expression += mid
for j in range(len(words) - 1, -1, -1):
    expression += words[j][0] * (words[j][1] // 2)
print(expression)
