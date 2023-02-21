n = int(input())
stack = []
for i in range(n):
    con = input().split()
    if con[0] == "push":
        stack.append(con[1])
    elif con[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif con[0] == "size":
        print(len(stack))
    elif con[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
