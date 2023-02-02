import sys
sys.stdin = open("요리사2953input.txt")

total = []
for i in range(5):
    score = list(map(int, input().split()))
    total.append(sum(score))
print(total.index(max(total))+1, max(total))