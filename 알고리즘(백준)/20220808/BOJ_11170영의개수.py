t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    cnt = 0
    for p in range(n,m+1):
        d = str(p)
        cnt +=d.count('0')
    print(cnt)