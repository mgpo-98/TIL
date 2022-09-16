import sys

sys.stdin = open("11021input.txt", "r")

t = int(input())

for i in range(1,t+1):
    a, b = map(int, input().split())
    print('Case', f'#{i}:', a+b)
