n = int(input())
ans = 0
while (n == 0) :
    if n % 5 == 0:
        ans += n//5
        break
    else :
        n -=2
        ans +=1
    if n<0 :
        break
print(ans)
 
        