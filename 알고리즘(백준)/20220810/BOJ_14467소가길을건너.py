t = int(input())
arr = {}
cnt = 0
for _ in range(t):
    n, m = map(int, input().split())
    if n not in arr :
        arr[n] = m
    else:
        if arr[n] != m:
            cnt += 1
            arr[n] = m
print(cnt)