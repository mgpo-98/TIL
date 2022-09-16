import sys

sys.stdin = open("7568덩치.txt", "r")

t = int(input())
people =[]

for i in range(t):
    x, y = map(int, input().split())
    people.append((x,y))
for j in people:
    rank = 1
    for k in people:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1
    print(rank, end =' ')