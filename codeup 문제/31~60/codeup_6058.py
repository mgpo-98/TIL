a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) and ((not c) and d))