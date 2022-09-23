i = 1
while True:
    li = map(int, input().split())
    if li[0] :
        break
    
    r, w, l = li
    t = r * 2
    piz = (w **2 + l ** 2) **0.5
    if t >= piz :
        print(f'Pizza {i} fits on the table.')
    else:
        print(f'Pizza {i} does not fit on the table.')
    i += 1