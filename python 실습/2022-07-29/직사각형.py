import sys

sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(1,t+1):
    d = 0
    a, b, c = map(int, input().split())
    if (a == b):
        d =c
    elif(a == c):
        d =b
    elif (b == c):
        d = a
    else :
        d =a 
    print(f'#{i} {d}')