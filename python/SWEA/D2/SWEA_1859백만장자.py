t = int(input())
for i in range(1,t+1):
    k = int(input())
    li = list(map(int,input().split()))[::-1]
    n_max = li[0]
    s = 0
    for j in range(1, k):
        if n_max > li[j]:
            s += n_max - li[j]
        else :
            n_max = li[j]
    print(f'#{i} {s}')
