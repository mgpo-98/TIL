n = int(input())
li = []
for i in range(n):
    a = list(map(input().split()))
    if a[0] == 'push' :
        li.append(a[0])

    elif a[0] == 'front' :
        if len(li) == 0 :
            print(-1)
        else :
            print(li[0])

    elif a[0] == 'back' :
        if len(li) == 0 :
            print(-1)
        else :
            print(li[-1])

    elif a[0] == 'size' :
        print(len(li))

    elif a[0] == 'empty ':
        if len(li) == 0 :
            print(1)
        else :
            print(0)
    elif a[0] == 'pop' :
        if len(li) == 0 :
            print(-1)
        else : 
            print(li.popleft())
        