from random import randrange
import sys
sys.stdin = open("얼마.txt", "r")

t = int(input())
for _ in range(t):
    s = int(input())
    n = int(input())
    cnt = 0
    for p in range(n):
        a, b = map(int, input().split())
        cnt += (a*b)
    print(s +cnt)

