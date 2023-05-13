length1, width1, length2, width2 = map(int, input().split())
ans = 0
flag = True
if length1 == width2 or length1 == width1:
    if length1 == width2 and length2 == width1:
        flag = False
        b = min(width2, width1) + min(width2, width1)
        print(max(length1, length2), b)
    elif length1 == length2 and width2 == width1:
        flag = False
        b = min(width2, length1) + min(length1, width1)
        print(max(length1, width1), b)
example = [[max(length1, length2), width2 + width1],
           [max(width1, width2), length2 + length1],
           [max(length1, width2), width1 + length2],
           [max(length2, width1), width2 + length1]]
maxim = example[0]
for j in range(1, 4):
    if maxim[0] * maxim[1] > example[j][0] * example[j][1]:
        maxim[0], maxim[1] = example[j][0], example[j][1]
if flag:
    print(maxim[0], maxim[1])
