t = int(input())
for i in range(1, t + 1):
    c = int(input())
    m = 0
    arry = list(map(int, input().split()))
    for p in range(101):
        if arry.count(p) == 0:
            continue
        elif arry.count(p) >= arry.count(m):
            m = p
    print(f"#{i} {m}")
