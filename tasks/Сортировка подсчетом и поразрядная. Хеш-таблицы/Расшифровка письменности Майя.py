import collections
import string
S = string.ascii_letters
n, m = map(int, input().split())
word = input()
alp = dict()
expression = input()
i = 0
window = dict()
cond = dict()

for j in range(52):
    window[S[j]] = 0
    cond[S[j]] = 0
for i in range(n):
    cond[word[i]] += 1
k = 0
answer = 0
for i in range(m):
    if i < n - 1:
        window[expression[i]] += 1
    elif i == n - 1:
        window[expression[i]] += 1
        for j in range(52):
            if window[S[j]] != cond[S[j]]:
                k += abs(window[S[j]] - cond[S[j]])
        if k == 0:

            answer += 1
    else:
        p = i - n
        if expression[p] != expression[i]:
            raz = abs(window[expression[p]] - cond[expression[p]])
            window[expression[p]] -= 1
            if abs(window[expression[p]] - cond[expression[p]]) < \
                    raz:
                k -= 1
            else:
                k += 1
            raz = abs(window[expression[i]] - cond[expression[i]])
            window[expression[i]] += 1
            if abs(window[expression[i]] - cond[expression[i]]) < \
                    raz:
                k -= 1
            else:
                k += 1
        if k == 0:
            answer += 1
print(answer)