from re import A
import sys

sys.stdin = open("1976_input.txt", "r")
h = 0
m = 0
n = int(input())
for i in range(1,n+1):
    a, b, c, d = map(int, input().split())
    h = a + c 
    m = b + d
    if m > 59:
            h += 1
            m -= 60
    if h > 12:
        h -= 12
    print(f'#{i}',h, m)

