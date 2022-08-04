import sys
sys.stdin = open("자리.txt", "r")
n = int(input())
li = []
r, c = 0, 0
cnt = 0
for i in range(n):
    li.append(list(input()))
for i in range(n):
    cnt = 0
    for j in range(n):
        if li[i][j] == '.':  # 가로
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            r += 1
for i in range(n):
    cnt = 0
    for j in range(n):
        if li[j][i] == '.': # 세로
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            c += 1
print(r, c)

