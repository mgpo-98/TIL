lst = list(map(int, input().split()))
c = [1,1,2,2,2,8]

for i in range(6):
    a = c[i] - lst[i]
    print(a, end=' ')
