n =int(input())
xy = []
for i in range(n):
    [a, b] = map(int,input().split())
    xy.append([a,b])
s_xy = sorted(xy)
for i in range(n):
    print(s_xy[i][0], s_xy[i][1])
