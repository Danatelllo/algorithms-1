n = int(input())
fib = [set() for j in range(10)]
fib[1].add(1)
fib[0].add(0)
maxim2 = 0
maxim = 1
for j in range(n):
    number = int(input())
    if number > maxim:
        result = 0
        while result < number:
            result = maxim + maxim2
            maxim2 = maxim
            maxim = result
            fib[maxim % 10].add(maxim)
        fib[result % 10].add(result)
        if result == number:
            print('Yes')
        else:
            print('No')
    elif number == maxim:
        print('Yes')
    else:
        if number in fib[number % 10]:
            print('Yes')
        else:
            print('No')