import sys

sys.stdin = open("input.txt", "r")

t = int(input()) #전체 케이스 수를 받는다

for i in range(1,t+1): #전체 케이스 수만큼 반복한다
    n = int(input()) #케이스 수
    a = list(map(int, input().split())) # 띄어쓰기로 나누고 리스트로 저장한다
    res = sum(a)//n  # 평균값 구하기 
    cnt = 0  # 카운트 값
    for j in a:  # a를 하나하나 가져 오며서 반복
        if j <= res:  #평균값보다 작으면
            cnt += 1 # 카운트 1을 올려라 
    print(f'#{i} {cnt}')