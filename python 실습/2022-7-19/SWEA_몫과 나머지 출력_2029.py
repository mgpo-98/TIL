#   import sys

#   sys.stdin = open("input.txt", "r")

t = int(input())

for i in range(1,t+1):
    a,b = map(int, input().split())
    print('#',i,a//b, a%b) 
