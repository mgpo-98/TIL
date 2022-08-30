
import sys

sys.stdin = open("3052나머지.txt", "r")
data =[]

for i in range(10):
    a = int(input())
    data.append(a % 42)
da =set(data)
print(len(da))
