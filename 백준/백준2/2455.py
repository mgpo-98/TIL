t = 0
li = []
for i in range(4):
    x, y = map(int, input().split())
    t = t - x + y 
    li.append(t)
    
print(max(li)) 