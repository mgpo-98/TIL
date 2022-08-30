import sys

sys.stdin = open("수정렬.txt", "r")

n = int(input())
li = []
for i in range(n):
    a = int(input())
    li.append(a)
li.sort()

for k in li:
    print(k)