from pprint import pprint
import sys

sys.stdin = open("성지키기.txt", "r")

n, m = map(int, input().split())
bin = []
cnt = 0
for _ in range(n):
    a = input()
    bin.append(a)
for p in range(n):
    if 'X' not in bin[p] :
        cnt += 1
for j in range(m):
    cnt1 = 0 
    for k in range(n):
        if list[k][i]
