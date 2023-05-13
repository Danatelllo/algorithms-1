def bin_search(start, end, width, length, quantity):
    mid = (start + end) // 2
    while start + 1 < end:
        condition = (mid // width) * (mid // length)
        if condition > quantity:
            end = mid
        if condition < quantity:
            start = mid
        if condition == quantity:
            y = mid // width
            x = mid // length
            if y == x:
                return max(length, width) * y
            if y != x:
                return max(y * width, x * length)

            return mid
        mid = (start + end) // 2
    if (start // width) * (start // length) >= quantity:
        return start
    else:
        return end


a, b, c = map(int, input().split())
print(bin_search(0, 10 ** 20, a, b, c))