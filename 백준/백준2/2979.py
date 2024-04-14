a, b, c = int(input())
time = [0]*100
cnt = 0
for _ in range(3):
    x, y = map(int, input().split())
    for i in range(x,y):
        time[i]+=1
        
for j in time:
    if j == 0 :
        cnt +=0
    elif j == 1:
        cnt+=a
    elif j == 2:
        cnt+=(b*2)
    elif j ==3:
        cnt+=(c*2)
print(cnt)          