n = int(input())
s = []

s.append(map(int, input().split()))
m = int(input())    
j = []
j.append(map(int, input().split()))

for i in m :
    if i in n :
        print(1, end=' ')
    else : 
        print(0, end=' ')