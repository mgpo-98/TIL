import sys

sys.stdin = open("대칭.txt", "r")
a, b = map(int, input().split())
la = set(map(int, input().split()))
lb = set(map(int, input().split()))

print(len(la-lb)+ len(lb-la))
