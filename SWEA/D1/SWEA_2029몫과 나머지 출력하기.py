import sys

sys.stdin = open("2029몫과 나머지 출력하기.txt", "r")

t = int(input())

for i in range(1,t+1):
    a, b =map(int, input().split())
    print(f'#{i}', a//b, a%b)