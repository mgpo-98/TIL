n = [i for i in range(1, 31)]

for _ in range(28):
    s = int(input())
    n.remove(s)
print(min(n))
print(max(n))
