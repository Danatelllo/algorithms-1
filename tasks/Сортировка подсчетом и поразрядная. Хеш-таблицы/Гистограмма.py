signs = dict()
with open('input.txt', 'r', encoding='utf8') as f:
    s = f.read().split()
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] not in signs:
                signs[s[j][i]] = 1
            else:
                signs[s[j][i]] += 1

maxim = max(signs.values())
n = maxim
s = sorted(signs)
for j in range(n):
    row = ''
    for i in s:
        if signs[i] == maxim:
            signs[i] -= 1
            row += '#'
        else:
            row += ' '
    maxim -= 1
    print(row)
print(*s, sep='')