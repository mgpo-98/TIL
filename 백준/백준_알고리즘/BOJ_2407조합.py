n, m = map(int, input().split())

value = 1
value2 = 1
for i in range(n, n-m, -1) :
  value *= i

for i in range(2, m + 1) :
  value2 *= i

print(value // value2)