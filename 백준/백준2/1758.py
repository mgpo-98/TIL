n = int(input())
cnt = 0
tip = []
for i in range(1,n+1):
    tip.append(t = int(input()))

tip.sort(reverse=True)    
for i in range(n):
    b=tip[i]-i
    if tip > 0 :
        cnt += tip
print(cnt)
     