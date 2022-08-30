# from re import T
# import sys

# sys.stdin = open("input2.txt", "r")

T = int(input())
for i in range(0,T):
    num = list(map(int, input().split()))
    print('#',T,round(sum(num)/10))
