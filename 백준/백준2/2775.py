t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    p = [i for i in range(1,n+1)]
    for x in range(k):
        new = [ ]
        for y in range(n):
            new.append(sum(p[:y+1]))
        p = new.copy()
    print(p[-1])