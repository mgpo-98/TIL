k, i = map(int, input().split())
for i in range(2, int(l)):
    if int(k) % i == 0:
        print("BAD", i)
        exit()

print("GOOD")
