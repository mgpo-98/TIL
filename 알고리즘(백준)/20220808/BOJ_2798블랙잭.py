import re


n, m = map(int, input().split())
max_total = 0
card = list(map(int, input().split()))
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = card[i] + card[j]+ card[k]
            if max_total < total <= m:
                max_total = total
           
print(max_total)


