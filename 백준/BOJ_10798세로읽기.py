import sys

sys.stdin = open("10798세로읽기.txt", "r")

word = list(input())
for i in range(15):
    for j in range(5):
        if j < len(word[i]):
            print(word[i][j], end=' ')