import sys

sys.stdin = open("input.txt", "r")

t = int(input())
for po in range(1,t+1):
    res = 0
    des = 0
    num = input().split()
    for i in range(len(num)):  # 길이만큼 반복
        
        if i % 2 == 0:  #홀수
            res += int(num[i])*2  # 2곱하고 합
           
            
        elif i % 2 == 1:  #짝수
            des += int(num[i]) # 합
                
    ri = res +des   # 짝수 홀수 합
    da =10-ri%10  # 10으로 나눈후 나머지를 10을뺀값이 N이다
    if da == 10:    # 0을 10으로 나누면 자꾸 10이나와 10을 0으로 바꿔준다
        da = 0
        print(f'#{po} {da}')
    else:
        print(f'#{po} {da}')