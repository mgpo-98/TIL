import sys
sys.stdin = open("N번째 큰수.txt", "r")
n = 3
t = int(input())

for _ in range(t):
    num = list(map(int, input().split()))
    num.sort()
    print(num[7])