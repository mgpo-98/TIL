import sys
sys.stdin = open('단어.txt', 'r')

t = int(input())
for _ in range(t):
    lst = input().split()
    for s in lst:
        print(s[::-1], end = ' ')
    print()