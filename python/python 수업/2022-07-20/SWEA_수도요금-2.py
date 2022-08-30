import sys

sys.stdin = open("input3.txt", "r")

a =int(input())
for i in range(1,a+1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    if R > W:
        B = Q
    else:
        B = Q + S*(W-R)
    print(f'#{i} {min(A,B)}')