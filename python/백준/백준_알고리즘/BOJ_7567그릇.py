g = list(input())
cnt = 0
for i in range(len(g)):
    if i == 0:
        cnt += 10
    elif g[i] == g[i-1]:
        cnt += 5
    else :
        cnt += 10 
print(cnt)