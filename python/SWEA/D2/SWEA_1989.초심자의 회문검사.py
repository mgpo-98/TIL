n = int(input())
for i in range(1, n + 1):
    a = input()
    if a == a[::-1]:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")
