
import sys
from tkinter.tix import Balloon

sys.stdin = open("공.txt", "r")

m = int(input())
cup = [0,1,2,3]
for _ in range(m):
    x, y = map(int, input().split())
    cup[x], cup[y] = cup[y], cup[x]
print(cup.index(1))