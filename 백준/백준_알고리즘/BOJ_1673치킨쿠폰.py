for i in range(3):
    n,k = map(intt, input().split())
    t = 0
    r = 0
    while n >= k:
        t = n//k
        r += k * t
        n = n % k + t
    t += n
    print(r)
