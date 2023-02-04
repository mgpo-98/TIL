arr = [1, 5, 2, 6, 3, 7, 4]
c = [2, 5, 3]
b = []
for i in range(c[0], c[1] + 1):
    b.append(arr[i])
print(b[c[2]])
