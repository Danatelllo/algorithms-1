def length(point1, point2):
    length1 = abs(point1[0] - point2[0])
    length2 = abs(point1[1] - point2[1])
    return (length1**2 + length2 ** 2) ** 0.5


n = int(input())
for j in range(n):
    coordinates = list(map(int, input().split()))
    points = sorted(zip(coordinates[::2], coordinates[1::2]))
    AB = points[1][1] - points[0][1]
    BC = -points[1][0] + points[3][0]
    CD = points[3][1] - points[2][1]
    AD = -points[0][0] + points[2][0]
    if AB == CD and AD == BC:
        print("YES")
    else:
        print("NO")