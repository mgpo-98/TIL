t = int(input())
for i in range(1,t+1):
    res = 0
    li = list(map(int, input().split()))
    for p in range(len(li)):
        if li[p] % 2 == 1 :
            res += li[p]
    print(f'#{i} {res}') 
        
