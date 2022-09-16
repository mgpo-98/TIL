import sys
from turtle import Turtle

sys.stdin = open("암기왕.txt", "r")

c = int(input())

for _ in range(c):
    n = int(input())
    y = set(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))
    for j in d :
        if j in y:
            print(1)
        else :
            print(0)