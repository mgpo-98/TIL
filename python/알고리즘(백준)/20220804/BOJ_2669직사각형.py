from random import randrange
import sys

sys.stdin = open("직각사각형.txt", "r")
board = [[0 for _ in range(10)] for _ in range(10)]
f = []
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1
cnt = 0
for r in board:
    cnt+= sum(r)
print(cnt)
