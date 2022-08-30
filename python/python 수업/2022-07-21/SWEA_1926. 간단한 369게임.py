n = int(input())
cnt = 0
for i in range(1,n+1):
    i = str(i)
    if (i in '3' or i in '6' or i in '9'):
        cnt += 1
        print('-'*cnt, end=' ')
    else:
        print(i, end =' ')