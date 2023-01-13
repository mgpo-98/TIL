c = int(input())
for i in range(c):
    s = list(map(int, input().split()))
    a = sum(s[1:]) / s[0]
    cnt = 0
    for p in s[1:]:
        if p > a:
            cnt += 1
    per = (cnt / s[0]) * 100
    print("%.3f" % per + "%")
