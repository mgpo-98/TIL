di = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
ret = 0
for i in range(len(a)):
    for j in di:
        if a[i] in j :
            ret += di.index(j) + 3
print(ret)
