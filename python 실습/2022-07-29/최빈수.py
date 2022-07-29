import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for po in range(1,t+1) :
    n = int(input())
    score = list(map(int, input().split())) #리스트 형태로 받는다
    data = [0] * 1001   # 0이 1001개 

    for i in score :
        data[i] += 1  #score값을 확인 하며 각 숫자가 몇개 인지 기록한다

    max_value = max(data) # data의 최대값을 저장
    result = []
    for i in range(len(data)) :
        if data[i] == max_value : 
            result.append(i)   #최대값을 요소를 res리스트에 저장

    print(f'#{po} {max(result)}')




