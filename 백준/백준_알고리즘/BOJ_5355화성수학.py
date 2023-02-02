from sys import flags


t = int(input())
for _ in range(t):
    m = list(map(str, input().split()))
    ans = 0
    for i in range(len(m)):
        if i == 0:
            ans += float(m[i])
        else:
            if m[i] == '#':
                ans -= 7
            elif m[i] == '%':
                ans +=5
            elif m[i] == '@':
                ans *= 3
    print('%0.2f' % ans) 