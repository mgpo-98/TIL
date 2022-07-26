import sys

sys.stdin = open("최소최대10818input.txt", "r")
a = int(input())
s = list(map(int, input().split()))
print(min(s),max(s))