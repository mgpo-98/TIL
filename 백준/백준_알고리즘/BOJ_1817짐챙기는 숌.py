n, m = map(int, input().split())

if n == 0:
    print(0)
else: 
    li = list(map(int,input().split()))
    cnt = 0
    res = 1
    for i in range(n-1,-1,-1):
        cnt += li[i]
        if cnt > m :
            res +=1
            cnt = li[i]
    print(res)