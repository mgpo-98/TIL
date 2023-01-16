t = int(input())
for i in range(2):
    a, s = map(input().split())

    for i in s:
        print(i * int(a), end="")
    print()
