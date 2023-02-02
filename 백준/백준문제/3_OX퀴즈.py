# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())
for i in range(t):
    a = list(input())
    score = 0 
    c = 1
    for j in a:
        if j == 'O':
            score += c
            c += 1
        else :
            c = 1
    print(score)
