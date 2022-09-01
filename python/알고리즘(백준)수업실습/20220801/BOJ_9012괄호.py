import sys

sys.stdin = open("괄호.txt", "r")

t = int(input())
for _ in range(t):
    a = list(input())
    if a.count('(') == a.count(')'):
        print('YES')
    else :
        print('NO')