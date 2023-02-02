

n = int(input())
book = {}
for _ in range(n):
    a = input()
    if a not in book:
        book[a] = 1
    else:
        book[a] +=1
list = []
f = max(book.values())
for i in book:
    if f ==book[i]:
        list.append(i)
list.sort
print(list[0])