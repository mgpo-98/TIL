n = int(input())
day = list(map(int, input().split()))

day.sort(reverse=True)
res=[]
for i in range(n):
    res.append(day[i]+1+i)
    
print(max(res)+1)