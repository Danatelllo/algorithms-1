a = int(input())
b = int(input())
c = int(input())
if c >= 0:
    if a == 0 and b == c ** 2:
        print("MANY SOLUTIONS")
    elif a == 0 and b != c ** 2:
        print("NO SOLUTION")
    elif a != 0 and (- b + c ** 2) % a == 0:
        print((- b + c ** 2) // a)
    else:
        print("NO SOLUTION")
else:
    print('NO SOLUTION')
