import sys

sys.stdin = open("input.txt", "r")

a = input()
for i in a:
    m = ord(i)-64
    print(m, end=' ')