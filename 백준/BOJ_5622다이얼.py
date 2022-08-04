num = ['ABX','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

ca = input()
res = 0
for i in range(len(ca)):
    for j in num :
        if i in j:
            res +=num.index(j) + 3
print(res)