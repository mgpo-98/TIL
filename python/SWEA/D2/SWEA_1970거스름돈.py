t = int(input())
for _ in range(1,t+1):
    print(f'#{_}')
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    c = [0] * 8
    for i in range(8):
        if n // money[i] > 0:
            c[i] += n//money[i]
            n = n % money[i]
    print(*c)