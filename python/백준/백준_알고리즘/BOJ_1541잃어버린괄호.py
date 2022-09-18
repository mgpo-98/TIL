a = input().split('-')
cnt = 0
list  = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    list.append(cnt)
n = list[0]
for i in range(1, len(list)):
    n -= list[i]
print(n)