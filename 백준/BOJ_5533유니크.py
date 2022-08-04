import sys

sys.stdin = open("유니크.txt", "r")

n = int(input())
li = []
score = [0] * n
for _ in range(n):
    a = list(map(str, input().split()))
    li.append(a)

for i in range(n):
    cnt =0 
    for j in range(3):
        print(li[i])
        print(li[i].count(li[i][j]))
            score[j] += 0
        else:
            score[j] += li[i][j]
for s in score:
    print(s)
