cnt = 1 
d = 0
t = int(input())
ma = []
for i in range(t):
    ma.append(int(input()))
mak = ma[-1]
for i in range(len(ma)-1,-1,-1):
    if ma[i] > mak:
        cnt += 1
        mak = ma[i]
print(cnt)