n, k = map(int, input().split())
m = []
for i in range(1,k+1):
    m.append(int(str(n*i)[::-1]))
print(max(m))