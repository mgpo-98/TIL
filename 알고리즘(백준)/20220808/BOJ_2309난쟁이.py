nan = []
for _ in range(9):
    nan.append(int(input())) 
total = sum(nan)
for i in range(8):
    for j in range(i+1,9):
        if 100 == total -(nan[i] + nan[j]):
            n1, n2 = nan[i], nan[j]
            break
nan.remove(n1)
nan.remove(n2)
nan.sort()
print(*nan)
    
    
        