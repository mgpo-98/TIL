n = int(input())
c = [0, 1]
for i in range(2, n + 1):
    m = c[i - 1] + c[i - 2]
    c.append(m)
print(c[n])
