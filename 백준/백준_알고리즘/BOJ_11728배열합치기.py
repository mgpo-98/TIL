m,n = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = a + b
s.sort()
print(*s) 
