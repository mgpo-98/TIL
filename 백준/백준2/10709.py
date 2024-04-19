n, m = map(int, input().split())
li = [input() for _ in range(n)]

for i in li :
    lst = [-1 for _ in range(m)]
    
    for j in range(m):
        if i[j] == 'c':
            lst[j] = 0 
    cnt = 0
    print(lst)
    for i in range(1,m):
        if lst[i] == 0:
            cnt = 0
        if lst[i-1] != -1 :
            if lst[i] !=0:
                cnt +=1
                lst[i] = cnt
  