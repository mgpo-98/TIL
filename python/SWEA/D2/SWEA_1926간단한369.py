n = int(input())
for i in range(1, n + 1):
    c = 0
    j = str(i)
    if "3" in j or "6" in j or "9" in j:
        c += j.count("3")
        c += j.count("6")
        c += j.count("9")
        for _ in range(c):
            print("-", end="")
        print(" ", end="")
    else:
        print(i, end=" ")
