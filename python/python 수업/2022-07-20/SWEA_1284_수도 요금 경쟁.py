import sys

sys.stdin = open("input3.txt", "r")

a =int(input())
for i in range(1,a+1):
    P,Q,R,S,W = map(int, input().split())
    A = P * W
    B = Q
    if R < W:
        B = Q * R +()
        
print(f'#{a}')
