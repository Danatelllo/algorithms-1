def get_hash(string):
    result = 0
    for char in string:
        result = (result + ord(char)) % 128
    return result

'''a'''
n = int(input())
a = 'd'
c = get_hash('d')
ans = ['d']
for j in range(4100):
    a += 'd'
    if get_hash(a) == c:
        ans.append(a)
for j in range(n):
    print(ans[j])