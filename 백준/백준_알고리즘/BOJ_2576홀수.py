num = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        num.append(n)
if sum(num) == 0:
    print(-1)
else :
    print(sum(num))
    print(min(num))