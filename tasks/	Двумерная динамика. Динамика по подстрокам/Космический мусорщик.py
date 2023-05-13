d_ = dict()
d_['N'] = input()
d_['S'] = input()
d_['W'] = input()
d_['E'] = input()
d_['U'] = input()
d_['D'] = input()
"NSWEUD"
s, n = (input().split())
n = int(n)
now = dict()
matrix = dict()
answer = 1
now[s] = 1
for j in range(n - 1):
    for i in now:
        for k in d_[i]:
            if k not in matrix:
                matrix[k] = 1 * now[i]
                answer += 1 * now[i]
            else:
                matrix[k] += 1 * now[i]
                answer += 1 * now[i]
    now = matrix
    matrix = dict()
print(answer)
