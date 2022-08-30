import sys

sys.stdin = open("공.txt", "r")

number = []
for i in range(10):
    number.append(int(input()))
print(sum(number)//10)
num = list(set(number))
x= []
for i in range(len(num)):
    x.append(number.count(num[i]))
print(num[x.index(max(x))])