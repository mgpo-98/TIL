from distutils.util import change_root
import sys

sys.stdin = open("input.txt", "r")

t = int(input()) #횟수 입력 
for i in range(1,t+1):    # 횟수만큼 반복
    a = input()      # 문자열 입력
    o = a[::-1]      # 문자 거꾸로 출력
    res = ''         # 빈 txt
    for j in range(len(o)):  
        if o[j] == 'b':             # 만약 j번째열에 b가있으면 d를 빈 리스트에 추가
             res += 'd'
        elif o[j] == 'd':
             res +='b'
        elif o[j] == 'p':
             res +='q'
        else:  res +='p'
    print(f'#{i} {res}')



