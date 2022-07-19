# import sys
# sys.stdin = open("input3.txt", "r")

t =int(input())

for i in range(1,t+1):
    a,b = map(int, input().split())
    print('#',i, end='' )
    if a < b :
        print('<')
    if a == b:
        print('=')
    else : 
        print('>')

