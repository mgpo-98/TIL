a, b, c = map(int, input().split())
s = [a,b,c]
for i in s:
    if i%2 == 0:
        print('even')
    else :
        print('odd')