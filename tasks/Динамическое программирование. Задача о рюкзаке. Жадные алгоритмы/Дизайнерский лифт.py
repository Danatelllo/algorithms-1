n = int(input())
arr = sorted(map(int, input().split()))
matrix = [0 for j in range(n + 1)]
matrix[1] = 1
answer = 0
if arr[0] == 1:
    print(n)
else:
    for j in range(3):
        if arr[j] + 1 < n:
            matrix[arr[j] + 1] = 1
            for i in range(2, n + 1):
                if i - arr[j] > 0 and matrix[i - arr[j]] == 1:
                    matrix[i] = 1
    print(sum(matrix))
