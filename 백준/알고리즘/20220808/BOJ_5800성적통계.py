from re import T
import sys
sys.stdin = open("성적.txt", "r")
k = int(input())
for _ in range(1,k+1):
    a = list(map(int, input().split()))
    s = a[0]
    max_gap = 0
    a = a[1:]
    a.sort(reverse=True)
    for i in range(s-1):
        gap = abs(a[i]-a[i+1])
        if gap > max_gap:
            max_gap = gap
    print(f'Class {_}')        
    print(f'Max {max(a)}, Min {min(a)}, Largest gap {max_gap}' )

    
