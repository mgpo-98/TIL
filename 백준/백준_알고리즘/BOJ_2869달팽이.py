a, b, v = map(int, input().split())
h = 0
s = 0
while True:
    s += 1
    h += a
    if h == v:
        print(s)
        break
    h -= b

print(s)
