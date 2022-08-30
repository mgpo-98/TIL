
from random import randrange
import sys
sys.stdin = open('바이러스.txt','r')

c = int(input())
p = int(input())
cmp = [[] for _ in range(c+1)]
for _ in range(p):
    v1, v2 = map(int, input().split())
    cmp[v1].append(v2)
    cmp[v2].append(v1)

print(cmp)