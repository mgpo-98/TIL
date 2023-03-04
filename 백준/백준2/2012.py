n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()    
c = 0
for i in range(1,n+1):
    c += abs(i-a[i-1])
print(c)



.