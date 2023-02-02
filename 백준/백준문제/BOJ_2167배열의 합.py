from re import L
import sys

sys.stdin = open("배열합.txt", "r")

n, m = map(int, input().split())
lst = []
for _ in range(n):
    a = list(map(int, input().split()))
    lst.append(a)
k = int(input())
for q in range(k):
    i, j, x, y = map(int, input().split())
    cnt = 0
    for b in range(i-1,x):
        for c in range(j-1,y):
            cnt+= lst[b][c]
    print(cnt) 
 