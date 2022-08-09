t = int(input())
Q1, Q2, Q3, Q4 = 0, 0, 0, 0 
AXIS = 0
for _ in range(1,t+1):
    n, m = map(int, input().split())
    if n == 0 or m == 0 :
        AXIS +=1
    elif n > 0 and m > 0:
        Q1 += 1
    elif n > 0 and m < 0:
        Q4 +=1
    elif n < 0 and m > 0:
        Q2 += 1
    else :
        Q3 += 1
print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')


    
