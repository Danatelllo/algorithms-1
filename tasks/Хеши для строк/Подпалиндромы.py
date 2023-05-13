ss = input()
'''Перебираем радиус и центры палиндрома для нечетных'''
start = 0
end = -10
ans = [0 for j in range(len(ss))]
for j in range(len(ss)):
    counter = 0
    '''В силу симметрии аналогично Z функции можно
    взять уже подсчитанное но аккуртано'''
    if j <= end:
        counter = min(ans[end - j + start], end - j)
    while counter + j <= len(ss) - 1 and j - counter >= 0 and \
            ss[counter + j] == ss[j - counter]:
        counter += 1
    ans[j] = counter
    if counter + j > end:
        end = j + counter
        start = j - counter
'''для четных чуть посложнее'''
start = 0
end = -10
ans2 = [0 for j in range(len(ss))]
for j in range(len(ss)):
    counter = 0
    '''В силу симметрии аналогично Z функции можно
    взять уже подсчитанное но аккуртано'''
    if j <= end:
        counter = min(ans2[end - j + start + 1], end - j + 1)

    while counter + j < len(ss) and j - counter - 1 >= 0 and \
            ss[counter + j] == ss[j - counter - 1]:
        counter += 1

    ans2[j] = counter
    if counter + j - 1 > end:
        end = j + counter - 1
        start = j - counter
'''c сотой попытке вроде уже получилось'''
print(sum(ans) + sum(ans2))