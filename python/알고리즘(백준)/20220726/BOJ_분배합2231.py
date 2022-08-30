n = int(input())
res = 0 
for i in range(1,n+1):
    a = list(map(int, str(i)))
    s = i +sum(a)
    if s == n :
        res = i
        break
print(res)