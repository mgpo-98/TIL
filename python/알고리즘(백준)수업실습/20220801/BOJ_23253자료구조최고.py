import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

for _ in range(m):
    p = int(input())
    a = list(map(int, input().split()))
 
    for i in range(p):
        print (a[i])
        # if a[i] > a[i+1]:
        #     print('Yes')
        
        # else :
        #     print('No')
            